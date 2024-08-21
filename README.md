# study_project
# MAP (My Asset Plan)


2024/08/21
AI 뉴스에 따른 호재/악재 예측
ㄴ KF-DeBERTa 모델: 최적의 파라미터 도출과 평가지표 산출. (ColabPro+로) 다시 진행
ㄴ 베스트 파라미터로 데이터 수 늘려서 다시 진행. 데이터불균형 문제 = 클래스 가중치 적용
ㄴ touch형식을 tensorflow형식으로 수정해 보기


2024/08/20
AI 뉴스에 따른 호재/악재 예측
ㄴ KF-DeBERTa 모델: 최적의 파라미터 도출과 평가지표 산출.
   하루종일 돌렸으나 안끝나서 켜놓고 갔으나, 컴퓨터 꺼짐


2024/08/19
AI 뉴스에 따른 호재/악재 예측
ㄴ KF-DeBERTa 모델: Huggingface의 transformers라이브러리와 Trainer클래스를 사용하여 파인튜닝하는 방식으로 진행. 최적의 파라미터 도출과 평가지표 산출 작업 필요

AI 과거지표에 따른 회귀분석을 통한 주가 예측
ㄴ Exponential Smoothing을 활용한 시계열 분석 사용법을 공부하고, 애플 주가 데이터를 적용하여 코드 작성 진행


2024/08/16
AI 뉴스에 따른 호재/악재 예측
ㄴ prophet 모델: 시계열 예측 모델에 적합하여 KF-DeBERTa모델로 변경
ㄴ KF-DeBERTa 모델: 벡터화 추출까지는 가능하나, touch에 적용할 형식으로 변환에 어려움
   그리드서칭과 지표 산출 필요

백앤드
ㄴ 회원가입 페이지 완료
ㄴ 이메일 인증코드 메일발송이 1번만 진행되는 부분 해결
   connection.close문제-> 생성된pool까지 모두 삭제되어 다음 전송시 풀이 없어서 발송이 안되었음
ㄴ FE단에서 보안상 중요한 작업을 진행하면 안되고, SERVER로 넘겨서 해야함
   이메일 인증코드를 FE페이지에서 생성하였는데, 유출될 우려가 있음

프론트앤드
ㄴ Form안에 있는 버튼은 타입을 버튼으로 설정해줘야 함. 그렇지 않으면 submit으로 되어 문제요인 가능


2024/08/12
아나콘다 환경 재설치 = KoBERT환경구축 실패로 재설치 mxnet numpy버전문제

데이터 전처리
ㄴ 쳇봇 질문 데이터 = 토큰화(komoran)+불용어처리+단어임베딩(KoBERT) Data\Data_Preprocessing\study_komoran_KoBERT.ipynb
ㄴ 쳇봇 질문 데이터 = 토큰화(komoran)+불용어처리+단어임베딩(KoElectra) Data\Data_Preprocessing\study_komoran_KoELECTRA.ipynb.ipynb

2024/08/07
프론트앤드
ㄴ 차트 그리기 연습 (양쪽인덱스 그래프) Web_FrontEnd/BiaxialLineChart.js
ㄴ 차트 그리기 연습 (이모티콘 포인트 그래프) Web_FrontEnd/CustomizedDotLineChart.js


2024/08/06
데이터 전처리
ㄴ 쳇봇 질문 데이터 = 토큰화(komoran)+불용어처리+단어임베딩(word2vector)

프론트앤드
ㄴ 차트 그리기 연습 Web_FrontEnd/ChartjsExample.js

2024/08/05
! 프로젝트 사용 깃 브런치 생성

백앤드
ㄴ 로그인 코드 작성


2024/08/02
! 프로젝트 사용 패키지 및 라이브러리 버전 맞추기

데이터 수집 - 쳇봇 학습데이터 생성
ㄴ 질문 분류를 위한 지출 관련 훈련 데이터 문장생성 (수정)

백앤드
ㄴ 회원가입 코드 작성


2024/08/01
데이터 분석 - 주가 vs 경제지표 지수
ㄴ Apple vs US 기준금리
ㄴ Apple vs US US GDP
ㄴ Apple vs US CB소비자 신뢰 지수
ㄴ Samsung vs CB소비자 신뢰 지수

데이터 수집 - 쳇봇 학습데이터 생성
ㄴ 질문 분류를 위한 지출 관련 훈련 데이터 문장생성

데이터 수집 - 개인 금융 데이터
ㄴ 개인 주식 매매 더미 데이터 생성 코드 작성


2024/07/31
데이터 분석 - 주가 vs 경제지표 지수
ㄴ Samsung vs US 기준금리
ㄴ Samsung vs US GDP

데이터 수집 - 개인 금융 데이터
ㄴ 개인 소비 더미 데이터 생성 코드 작성


2024/07/30
데이터 수집 - 개인 금융 데이터
ㄴ 개인 자산 더미 데이터 생성 코드 작성
ㄴ 개인 은행 입출금 데이터 생성 코드 작성


2024/07/29
데이터 분석 - 주가 vs 경제지표 지수
ㄴ Apple vs Gold rate

데이터 수집 - 개인 금융 데이터
ㄴ 개인 금융 더미 데이터 생성 코드 작성


2024/07/26
API 데이터 수집
ㄴ 한국은행API 데이터


2024/07/25
개인금융 데이터 API연동
ㄴ 마이데이터 : 연동 실패 (자본금 5억 이상 사업자에게 테스트 서버 재공)


2024/07/24
API 데이터 확인
ㄴ 한국은행API 데이터 데이터프레임화 코드 작성


2024/07/23
API 데이터 조사
ㄴ 한국은행 https://ecos.bok.or.kr/api/#/DevGuide/StatisticalCodeSearch
    한국지표 대부분
ㄴ 누리집: 외교부 https://www.data.go.kr/data/15099538/openapi.do
    나라별 GDP, 경제성장률, 물가상승률, 실업률, 수출수입액
ㄴ 야후 파이낸스 # !pip install yfinance  # import yfinance as yf
    기업 주가 및 정보


... 2024/07/22 - 주제 선정