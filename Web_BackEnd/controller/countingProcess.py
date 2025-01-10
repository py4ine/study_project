from yolox.tracker.byte_tracker import BYTETracker
from ultralytics.utils import LOGGER
from ultralytics import YOLO
from argparse import Namespace
import numpy as np
import websockets
import warnings
import requests
import asyncio
import torch
import json
import cv2

# yolo 로그 메시지 비활성화
LOGGER.disabled = True

# 경고 메시지 무시
warnings.filterwarnings("ignore", category=UserWarning)

# YOLOv8 모델 로드 (사전 학습된 COCO 데이터셋 사용)
model = YOLO('./yolov8n.pt')  # 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt' 중 선택 가능

# ByteTrack 설정
tracker_args = {
    'track_thresh': 0.5,  # 객체를 새로 추가할 때 사용되는 신뢰도 임계값
    'high_thresh': 0.6,   # 탐지된 객체의 신뢰도가 high_thresh보다 크면 "고신뢰 탐지"로 간주.
    'match_thresh': 0.8,  # 추적된 객체와 새 탐지된 객체 간의 매칭 기준(IOU, Intersection-over-Union).
    'track_buffer': 30,  # 객체 추적을 중단하기 전에 대기하는 프레임 수
    'mot20': False,  # MOT20 데이터셋 호환 모드를 활성화 여부. 복잡한 군중 추적 = True
}

# 딕셔너리를 Namespace로 변환
tracker_args = Namespace(**tracker_args)
tracker = BYTETracker(tracker_args)

# 영상 파일 열기
url = 'rtsp://210.99.70.120:1935/live/cctv002.stream'
cap = cv2.VideoCapture(url)

# 초기 설정
count_num = 0
TARGET_CLASS = [2, 5, 7]
skip_frames = 5  # 5프레임마다 한 번씩 처리
server_url = "http://localhost:8080/counting/update_count"  # 전송 서버 URL

async def video_stream(websocket, path='.'):
    global count_num
    global cap
    object_tracks = {}
    frame_count = 0

     # 스트림 연결 시도
    def connect_stream():
        global cap
        cap = cv2.VideoCapture(url)
        if not cap.isOpened():
            print("Failed to connect to RTSP stream. Retrying in 5 seconds...")
            return False
        return True
    
    # 처음 연결 시도
    while not connect_stream():
        await asyncio.sleep(1)  # 5초 후 재시도

    try:
        while True:
            # 첫 번째 프레임에서 프레임 크기 초기화
            ret, frame = cap.read()
            if not ret:  # 첫 번째 프레임 읽기 실패 시 프로그램 종료
                print("RTSP 스트림을 열 수 없습니다.")
                cap.release()
                exit()

            # 비디오 프레임 사이즈
            frame_height, frame_width = frame.shape[:2]
            mid_x = frame_width // 2  # 화면 중간 x좌표 계산
            mid_y = frame_height // 2  # 화면 중간 y좌표 계산

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                if frame_count % skip_frames != 0:  # 프레임 스킵
                    continue
                if frame_count % 1000 == 0:  # 1000프레임마다 스트림 재연결
                    cap.release()
                    cap = cv2.VideoCapture(url)

                # YOLOv8 객체 탐지
                results = model(frame)
                detections = []

                for result in results:
                    for box in result.boxes:
                        x1, y1, x2, y2 = box.xyxy[0].tolist() #map(float, box.xyxy[0].tolist())  # 좌표를 계산하는 부분
                        confidence = float(box.conf[0])  # tensor -> float 변환  # 신뢰도
                        class_id = int(box.cls[0])  # 클래스id
                        if confidence > 0.5:# and class_id in TARGET_CLASS:  # 신뢰도 필터링
                            detections.append([x1, y1, x2, y2, confidence, class_id])  # [x1, y1, x2, y2, confidence, class_id]
                
                # ByteTrack 추적
                img_info = (frame_height, frame_width)  # 이미지 정보
                img_size = (frame_width, frame_height)  # 이미지 크기

                if len(detections) == 0:
                    detection_array = np.empty((0, 5), dtype=float)  # 빈 배열 생성
                else:
                    detection_array = np.array(detections, dtype=float)  # 넘파이 버전 이슈로 dtype수정
                detection_tensor = torch.from_numpy(detection_array).type(torch.float32)  # numpy 배열을 PyTorch Tensor로 변환
                online_targets = tracker.update(detection_tensor, img_info, img_size)
                
                # 추적 결과 시각화
                for target in online_targets:
                    x1, y1, w, h = target.tlwh  # 바운딩 박스 좌표 및 크기
                    x1, y1, x2, y2 = int(x1), int(y1), int(x1 + w), int(y1 + h)  # 박스 좌표 변환

                    # YOLO 모델의 입력 이미지 크기 (전처리 시 사용한 크기)
                    input_width, input_height = 1080, 720  # 모델 입력 크기
                    # 이미지 크기 비율 계산
                    scale_x = frame_width / input_width  # 가로 비율
                    scale_y = frame_height / input_height  # 세로 비율
                    # 원본 이미지 크기에 맞게 좌표 변환
                    x1 = int(x1 * scale_x)
                    y1 = int(y1 * scale_y)
                    x2 = int(x2 * scale_x)
                    y2 = int(y2 * scale_y)
                    scale_w = int(w * scale_x)
                    scale_h = int(h * scale_y)

                    # 중심점 계산
                    center_x = int(x1 + scale_w / 2)
                    center_y = int(y1 + scale_h / 2)
                    
                    # 고유 객체 ID (ByteTrack에서 track_id 사용)
                    object_id = target.track_id

                    # 이전 위치와 비교하여 이동 방향 계산
                    if object_id in object_tracks:
                        prev_center_x, prev_center_y = object_tracks[object_id]

                        # 위쪽 → 아래쪽 이동
                        if prev_center_y < mid_y and center_y >= mid_y:
                            count_num += 1

                        # 아래쪽 → 위쪽 이동
                        elif prev_center_y > mid_y and center_y <= mid_y:
                            count_num -= 1

                    # 현재 위치 저장
                    object_tracks[object_id] = (center_x, center_y)
                    
                    # 바운딩 박스 그리기
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # source, 왼위좌표, 오아좌표, 선 색상, 선 두께
                    cv2.putText(frame, f"ID: {object_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)  # 중심점 표시
                
                # 서버로 카운트 전송
                try:
                    response = requests.post(server_url, json={"count": count_num})
                    print(f"Server response: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to send data to server: {e}")
                
                # 영상 중간 부분에 가로선 그리기
                cv2.line(frame, (0, mid_y), (frame_width, mid_y), (255, 0, 0), 1)  # (255, 0, 0)은 파란색, 두께는 1
                
                # 현재 카운팅 값을 화면에 표시
                cv2.putText(frame, f"Count: {count_num}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # 프레임을 JPEG로 인코딩
                _, buffer = cv2.imencode('.jpg', frame)

                # WebSocket으로 전송
                try:
                    await websocket.send(buffer.tobytes())
                except websockets.exceptions.ConnectionClosed:
                    print("WebSocket connection closed.")
                    break

                # FPS 제한
                await asyncio.sleep(0.033)  # 약 30 FPS

                # 영상 프레임 보여주기
                cv2.imshow('Detection', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

# WebSocket 서버를 시작하고 프로그램이 종료되지 않도록 유지
async def main():
    try:
        host_address = 'localhost'
        websoket_port = 9988
        start_server = websockets.serve(video_stream, host_address, websoket_port)  # WebSocket 서버 생성
        await start_server
        await asyncio.Future()  # 프로그램을 무기한 대기 상태로 유지(서버가 계속 실행되도록)
    except Exception as e:
        print(f"Error starting WebSocket server: {e}")

if __name__ == "__main__":
    asyncio.run(main())  # 이벤트 루프를 자동으로 생성하고 실행