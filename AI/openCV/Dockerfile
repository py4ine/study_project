# Python 3.8 슬림 버전 이미지를 기반으로 설정
FROM python:3.8-slim

# 작업 디렉토리 설정 (컨테이너 내부의 /app 디렉토리에서 작업)
WORKDIR /app

# 필수 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \        # GCC와 GNU 관련 컴파일 도구
    cmake \                  # CMake: 빌드 자동화 도구
    git \                    # Git: ByteTrack 클론 및 기타 버전 관리용
    ninja-build \            # Ninja: 빠른 빌드 시스템
    ffmpeg \                 # FFmpeg: 미디어 처리 라이브러리 (OpenCV 사용 가능)
    libsm6 \                 # OpenCV 종속성 (libSM 관련)
    libxext6 \               # X11 관련 라이브러리 (OpenCV 종속성)
    && rm -rf /var/lib/apt/lists/* # 캐시 데이터 제거로 이미지 크기 축소

# Python pip 업그레이드
RUN pip install --no-cache-dir --upgrade pip

# 1단계: NumPy 최신 버전 설치 및 다른 패키지 설치
COPY requirements_temp.txt . # 임시 요구 사항 파일 복사
RUN pip install --no-cache-dir -r requirements.txt

# 2단계: NumPy를 1.19.5로 다운그레이드 및 관련 패키지 설치
RUN pip install --no-cache-dir numpy==1.19.5 scipy==1.7.3 matplotlib==3.4.3

# 프로젝트 코드 복사 (로컬 디렉토리 내용을 컨테이너 내부 /app에 복사)
COPY . .

# ByteTrack 설치
RUN git clone https://github.com/ifzhang/ByteTrack.git \ # ByteTrack 레포지토리 클론
    && cd ByteTrack \                                    # ByteTrack 디렉토리로 이동
    && python3 setup.py develop                         # ByteTrack 설치

# FastAPI 서버가 실행될 포트 (8000번 포트 노출)
EXPOSE 8000

# 컨테이너 시작 시 실행될 명령어 (FastAPI 서버 실행)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]