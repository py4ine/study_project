from fastapi.responses import StreamingResponse
from fastapi import FastAPI, WebSocket
from yolox.tracker.byte_tracker import BYTETracker
from ultralytics import YOLO
from argparse import Namespace
import numpy as np
import asyncio
import torch
import cv2

# FastAPI 애플리케이션 생성
app = FastAPI()

# YOLO 및 ByteTrack 초기화
model = YOLO('./yolov8n.pt')
tracker_args = Namespace(track_thresh=0.5, hight_thresh=0.6, match_thresh=0.8, track_buffer=30, mot20=False)  # ByteTrack 설정
tracker = BYTETracker(tracker_args)  # ByteTrack 인스턴스 생성

# 전역 변수 초기화
count_num = 0
TARGET_CLASS = [2, 5, 7]
url = 'rtsp://210.99.70.120:1935/live/cctv002.stream'
cap = cv2.VideoCapture(url)  # RTSP 스트림 열기

# RTSP 유지 및 카운팅 업데이트
async def update_count():
    global count_num
    global cap
    object_tracks = {}  # 객체의 이전 위치를 저장하는 딕셔너리

    while True:
        if not cap.isOpened():
            print("RTSP 스트림 재연결 중")
            cap.release()  # 스트림 해제
            await asyncio.sleep(1)  # 1초마다 재연결 시도
            cap = cv2.VideoCapture(url)  # 스트림 재연결
            continue

        ret, frame = cap.read()  # 프레임 읽기
        if not ret:
            print("프레임 읽기 실패. RTSP 스트림 재연결 중")
            await asyncio.sleep(1)  # 1초마다 재연결 시도
            continue

        print(f"Frame shape: {frame.shape if frame is not None else 'None'}")
        # 객체 탐지
        results = model(frame)  # YOLO로 객체 탐지
        print(f"YOLO Results: {results}")
        detections = []  # 객체 탐지 결과를 저장할 리스트
        print(f"Detections: {detections}")
        
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()  # 객체의 좌표 추출
                confidence = float(box.conf[0])  # 객체의 신뢰도 추출
                class_id = int(box.cls[0])  # 객체의 클래스 ID 추출
                if confidence > 0.5:  # 신뢰도가 0.5 이상인 객체만 탐지
                    detections.append([x1, y1, x2, y2, confidence, class_id])  # 탐지 결과 저장

        # ByteTrack으로 객체 추적
        img_info = (frame.shape[0], frame.shape[1])  # 이미지 정보
        detection_array = np.array(detections, dtype=float) if detections else np.empty((0, 6), dtype=float)  # 탐지 결과를 NumPy 배열로 변환
        detection_tensor = torch.tensor(detection_array, dtype=torch.float32)  # NumPy 배열을 PyTorch 텐서로 변환
        online_targets = tracker.update(detection_tensor, img_info, frame.shape)  # ByteTrack으로 객체 추적
        print(f"online_targets: {online_targets}")

        # 객체 ID를 기준으로 카운트 업데이트
        for target in online_targets:
            track_id = target.track_id  # 객체 ID
            x1, y1, w, h = target.tlwh  # 객체의 좌표 및 크기
            x2, y2 = int(x1 + w), int(y1 + h)  # 객체의 좌표 및 크기
            center_y = (y1 + h) // 2  # 객체의 중심 Y 좌표

            # 객체가 중간선을 넘어갔는지 확인
            if track_id in object_tracks:
                prev_y = object_tracks[track_id]  # 이전 프레임의 중심 Y 좌표
                mid_y = frame.shape[0] // 2  # 이미지의 중심 Y 좌표

                if prev_y < mid_y <= center_y:  # 위 -> 아래로 이동
                    count_num += 1  # 카운트 증가
                elif prev_y > mid_y >= center_y:  # 아래 -> 위로 이동
                    count_num -= 1  # 카운트 감소

            # 현재 객체 위치 저장
            object_tracks[track_id] = center_y

        await asyncio.sleep(0.5)  # 0.5초마다 카운트 업데이트

# root 경로 접속 시,
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# favicon.ico 요청 시,
@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available"}

# 카운트 API
@app.get("/counting")
async def update_count():
    return {'count': count_num}

# 웹소켓 API
@app.websocket('/stream')
async def video_stream(websocket: WebSocket):

    # 웹소켓을 통해 클라이언트로 영상 전송
    await websocket.accept()  # 웹소켓 연결 수락
    while True:

        if not cap.isOpened():
            print("RTSP 스트림이 닫혀있습니다. 연결을 재시도합니다.")
            await asyncio.sleep(1)
            continue

        ret, frame = cap.read()  # 프레임 읽기
        if not ret:  # 프레임 읽기 실패 시
            print("RTSP 스트림을 열 수 없습니다.")
            await asyncio.sleep(0.033)  # 30FPS 속도로 재시도
            continue

        _, buffer = cv2.imencode('.jpg', frame)  # 프레임을 JPEG로 인코딩
        await websocket.send_bytes(buffer.tobytes())  # 웹소켓으로 전송
        await asyncio.sleep(0.033)  # 30FPS 속도로 전송


# 메인 함수
if __name__ == '__main__':
    import uvicorn  # FastAPI 서버 실행을 위한 라이브러리
    loop = asyncio.get_event_loop()  # 비동기 이벤트 루프 생성
    loop.create_task(update_count())  # 비동기 작업으로 카운트 업데이트 실행
    uvicorn.run(app, host='localhost', port=8000)  # FastAPI 서버 실행