# study_project
# MAP (My Asset Plan)

10/22
AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 삼성전자)
ㄴ 단어 배치 렌덤 교체 방법으로 악제 데이터 증강하여 시도하였으나 추가 해결 필요


10/21
AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 삼성전자)
ㄴ 단어 배치 렌덤 교체 방법으로 악제 데이터 증강하여 시도하였으나 추가 해결 필요


10/18
프로젝트 ReadMe 정리
ㄴ 회원가입 페이지 기능 정리
 + email 중복 체크
 + email 코드 인증
 + 회원가입 DB 저장

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 삼성전자)
ㄴ 호재 데이터에 맞춰 악재 데이터 2배수 증강. 모든 데이터를 악재로 인식


10/16
프로젝트 발표
AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 삼성전자)
ㄴ 원본 데이터로 먼저 시도. 모든 데이터를 호재로 인식


10/11 ~ 10/15
프로젝트 발표 준비
AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 비트코인)
ㄴ 단어 배치 렌덤 교체 방법으로 데이터 증강하여 데이터 불균형 문제 해결


10/10
AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 비트코인)
ㄴ 호재 데이터 언더샘플링, 악제 데이터 오버샘플링 동시에 적용하여 보강하였으나 차도가 없음
ㄴ K-fold 적용하여 진행해 볼 예정


10/7
AI 챗봇
ㄴ 재무 지출/소득/입출금/예적금 엔티티에 대한 문장생성 코드를 1개 함수로 업데이트


10/4
AI 챗봇
ㄴ 재무로 분류된 의도의 대출/예산 엔티티 질문에 대한 답변 문장생성 추가 작성


10/1
AI 챗봇
ㄴ 지출/소득/입출금 엔티티 질문의 미래시점 고정값에 대한 답변 문장생성 시 아직 발생하지 않은 데이터가 필요하기 때문에, 과거 고정값으로 정해진 데이터를 DB에서 가지고오도록 하여 처리
ㄴ 이번달의 경우는 날짜 엔티티가 현재 월로 뽑히기 때문에 한달 전까지의 데이터로, 다음 달이나 n월은 엔티티가 다음 월로 뽑히기 때문에 2달전으로 세팅해야 정상적으로 처리가 되었음.
ㄴ DB에서 검색된 날짜들도 모두 과거 데이터였기 때문에 현재나 미래 시점의 날짜로 변경해서 처리를 해줘야 했음 

백앤드
ㄴ 자산부분 데이터 크기 이슈로 DB에서 데이터 타입을 BIGINT로 변경하니, DB에서 값을 조회하여 FE화면으로 넘기기 위해 JSON.stringify()로 변경하는 방식에 문제가 생겨서 사용자 정보를 FE로 넘기지 못하여  기능 오류가 발생. BIGINT타입의 값을 문자열 형식으로 먼저 변환 후 처리하도록 수정하여 해결


10/1
AI 챗봇
ㄴ 재무로 분류된 의도의 입/출금 엔티티 질문에 대한 답변 문장생성 작성


9/30
AI 챗봇
ㄴ 재무로 분류된 의도의 소득 엔티티 질문에 대한 답변 문장생성 작성


9/28
AI 챗봇
ㄴ 재무로 분류된 의도의 지출 엔티티 질문에 대한 답변 문장생성 작성


9/27
AI 챗봇
ㄴ 재무로 분류된 의도의 지출 엔티티 질문에 대한 답변 문장생성 작성중
ㄴ 사용자 질문을 -> Node서버로 받아 -> 파이썬 모델을 통한 의도인식 -> 파이썬 코드를 통한 엔티티 추출 -> 파이썬 코드를 통한 쿼리문 반환 -> Node서버에서 쿼리문을 이용해 DB조회 -> 파이썬 코드를 통하여 DB조회된 데이터를 가공하여 문장 생성 -> Node서버에서 FE화면으로 출력
 

9/26
AI 챗봇
ㄴ 질문에 따른 페이지 링크 답변 로직 작성
ㄴ 의도인식 분류 모델 적용

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 비트코인)
ㄴ 데이터 오버샘플링을 통하여 보강중


9/25
AI 챗봇
ㄴ 재무 엔티티 패턴2에 대한 쿼리문 작성
ㄴ 프로젝트 마무리 일정에 맞춰 답변에 대한 문장생성이 불가능 할 수 있어, 대비책으로 1차 질문에 따른 페이지 링크를 프레임안에 담아 답변을 줄 수 있도록하고, 2차 버전업으로 문장생성 답변을 줄 수 있도록 조정

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 애플, 비트코인)
ㄴ 데이터 오버샘플링을 통하여 보강중. 애플 완료


9/24
AI 챗봇
ㄴ 재무 엔티티, sell부분 추가 완료, 입출금 관련 오류 사항 수정

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 애플)
ㄴ 데이터 오버샘플링을 통하여 보강중

유스케이스 다이어그램 작성


9/23
AI 챗봇
ㄴ 재무 엔티티, 오류 사항 업데이트

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa / 애플)
ㄴ 데이터 오버샘플링을 통하여 보강중

백앤드
ㄴ JWT토큰 방식에서 세션으로 변경한 이후 마이페이지 회원탈퇴 기능 리뷰 중, 세션에 저장된 ID를 통해 이메일을 검색하여 삭제하는 방식으로 되어 있는 것을 발견하여, 세션 저장 ID만으로 삭제 할 수 있도록 간소화


9/20
AI 챗봇
ㄴ 재무 엔티티 buy일 경우, 단어에 따라 주식과 소비 두 파트로 연결되는 쿼리문 추가
ㄴ sell부분 추가 필요


9/19
AI 챗봇
ㄴ 재무 엔티티 주식파트 쿼리문 업데이트


9/17
AI 챗봇
ㄴ 날짜 형식에 따른 앤티티 쿼리 추출문 업데이트
ㄴ 재무 엔티티 주식 관련 쿼리 추출문 추가
ㄴ 주식은 소비 카테고리와 테이블과 컬럼명이 달라서 날짜 부분의 쿼리문 변경 필요


9/16
AI 챗봇
ㄴ 앤티티 쿼리 추출문에 날짜 추가 코드 업데이트
ㄴ 날짜 형식에 따른 문제 보강 필요

9/13
백앤드
ㄴ 주식 예측 그래프 페이지 서버연결
ㄴ FE 지식이 부족하여 데이터의 변수 지정 등에 어려움이 있었음. FE지식도 어느정도는 필요함을 느낌

9/12
AI 챗봇
ㄴ 엔티티가 2개 이상일 경우, 엔티티 중 더 좁은 범위의 엔티티를 더 높은 숫자를 주고, 높은 숫자의 엔티티에 대한 대답을 해줄 수 있도록 고려
ㄴ 1개의 엔티티에 2가지 질문이 들어있을 경우도 발생


9/11
AI 챗봇
ㄴ 사용자가 질문할 수 있는 예상질문들을 기반으로 앤티티 추가 작성. Finance 관련 주요 앤티티 패턴과 사용자에게 보여줘야 할 형식으로 패턴을 나누어, DB에서 데이터를 추출할 주요 앤티티 패턴과 FE로 보여줄 형식 앤티티 추출
ㄴ 추출한 앤티티를 기반으로 쿼리문 작성
ㄴ 엔티티가 2개 이상 추출될 경우 처리 방안에 대해 고민이 필요 


9/9
AI 챗봇
ㄴ 의도인식을 Finance로 분류한 질문에 대한 앤티티 값을 찾는 코드 작성중
ㄴ 사용자가 질문할 수 있는 경우의 수가 무수히 많아 예상질문을 뽑고 거기에 대한 엔티티를 추출하는데 어려움이 많았음


9/6
Dev/Ops
ㄴ ubuntu문제로 nginx 도커 실행시 localhost접속이 안되는 현상으로 환경 재설치
ㄴ Linux 환경에서 FE, BE, DB Docker 이미지화 시도. FE 이미지화까지 성공
ㄴ AWS EC2 인스턴스 설정 및 보안키 putty 연결


9/5
Dev/Ops
ㄴ Linux 환경에서 FE, BE, DB Docker 이미지화 시도

9/4
백앤드
ㄴ 회원가입 페이지 수정 완료. user_ID가 이미 FK로 지정되어 있었고, 테이블에 생성된 것이 안보일 뿐이었고, user_ID로 매칭하여 정보를 넣을 수 있었음
ㄴ 마이페이지 수정 완료. 
ㄴ 회원탈퇴 관련 User정보를 가져올 수 없어서 진행 못하였던 부분은 JWT토큰에서 유저 이메일 정보를 같이 토큰화하여 브라우저에 쿠키로 저장하고, 쿠키 파일을 받아 토큰을 풀어 정보를 얻을 수 있도록 설정하여 해결 완료

AI 챗봇
ㄴ 사용자의 질문으로 부터 추출된 앤티티에 날짜 개념이 여러개 있을 때, 어떻게 처리할지 논의
 

9/3
AI파트 Git 병합 진행

백앤드
ㄴ DB 테이블 변경으로 회원가입 페이지 수정 중. 회원가입 관련 테이블이 1개에서 3개로 늘어나서 쿼리를 3개로 나눠서 작성 진행. 메인 user_ID만 자동생성되고 다른테이블의 ID는 자동생성이 안되는 문제로 담당자와 커뮤니케이션 필요


9/2
백앤드
ㄴ 마이페이지 회원정보 수정 DB적용 완료
ㄴ 회원탈퇴 관련 REST API Delete는 CORS 정규정책사 body내용을 보낼 수 없어서 DB 삭제에 어려움 봉착. 로그인시 세션에 userID를 저장하여 REST API 통신으로 같이 보내려고 하였으나, undifined 상태로 해결방안 모색 중

AI 뉴스에 따른 호재/악재 예측 (KF-DeBERTa 모델)
ㄴ 파인튜닝한 모델을 사용하여 예측하는 함수 작성


2024/08/28
백앤드
ㄴ 마이페이지 접속 시 DB에서 user정보를 가지고와 각 항목창에 넣어주기 완료

AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ 오버샘플링한 전체 데이터의 최적 파라미터 찾아 모델링


2024/08/27
하드포멧 및 프로그램 재설치

AI 과거지표에 따른 회귀분석을 통한 주가 예측 (Exponential Smoothing 모델)
ㄴ 학습한 모델 저장/불러오기 및 날짜입력에 따른 예측값 도출 함수 작성

AI 뉴스에 따른 호재/악재 예측 (코인 / KF-DeBERTa 모델)
ㄴ 오버샘플링한 전체 데이터의 최적 파라미터 찾아 모델링


2024/08/26
AI 과거지표에 따른 회귀분석을 통한 주가 예측 (Exponential Smoothing 모델)
ㄴ 모델에 적합한 학습기간을 반영하여 추가작업 진행
ㄴ 애플 = 6개월 기간을 훈련7:테스트3으로 나누어 진행. R²=0.60에서 0.82로, MSE=160.44에서 20.90으로 개선
ㄴ 삼성 = 4개월 기간을 훈련7.5:테스트2.5로 나누어 진행. R²=0.30에서 0.86로, MSE=38813472.27에서 923547.79로 개선


2024/08/23
AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ 모든 뉴스를 '호재'로만 분류하여 데이터 불균형을 해결하기 위해 클래스 가중치를 0.95배로 적용하였더니, '호재'와 '악재'를 구분함.
ㄴ '호재'를 '악재'보다 조금 더 잘 구분하나, 만족스럽지 못함. Accuracy: 0.47, F1 Score: 0.51 -> 데이터 가중치를 0.97로 조정
ㄴ '악재'는 잘 구분하나 '호재'를 거의 구분 못함. Accuracy: 0.41, F1 Score: 0.08 -> 데이터 가중치를 0.96으로 조정
ㄴ 모든 뉴스를 다시 '호재'로만 분류. Accuracy: 0.57, F1 Score: 0.72 -> 다른 방법이 필요

AI 뉴스에 따른 호재/악재 예측 (삼성 / KF-DeBERTa 모델)
ㄴ 최적의 파라미터 도출과 평가지표 산출
ㄴ 베스트 파라미터로 데이터 수 늘려서 다시 진행. Accuracy: 0.49, F1 Score: 0.56 -> '악재'분류가 부족하여, '호재'가중치 0.95로 수정
ㄴ '악재'로만 구분하여, 가중치를 0.97로 수정하여 진행. Accuracy: 0.53, F1 Score: 0.42 -> '호재'분류가 부족하여, 가중치 0.98로 수정
ㄴ '악재'로만 분류 Accuracy: 0.50, F1 Score: 0.0 -> 가중치 0.99로 수정 -> '호재'로만 분류


2024/08/22
AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ 데스크탑으로 실행하였을 때, 120시간이 소요될 예정. 시간소요를 줄일 방법이 필요
ㄴ 모든 뉴스를 '호재'로만 분류하여 데이터 불균형을 해결하기 위해 클래스 가중치를 1.5배로 적용하였으나, 계속 '호재'로만 분류
ㄴ 총 9,156개 (호재5,334/악재3,882)를 훈련/테스트 8:2로 나누어서 학습 진행
ㄴ 데이터 불균형 문제가 해결되지 않았거나 모델 적용에 문제가 있는 듯. 아니면 애초의 데이터의 문제가 있을 수도 있고 데이터의 수가 부족해서 그럴지도..


2024/08/21
AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ 최적의 파라미터 도출과 평가지표 산출. (Colab으로) 다시 진행
ㄴ 베스트 파라미터로 데이터 수 늘려서 다시 진행. 데이터불균형 문제 = 클래스 가중치 적용
ㄴ Colab L4로 진행하였을 때, 진행시간 2시간 소요. 모든 뉴스를 '호재'로만 분류하는 결과. 
ㄴ touch형식을 tensorflow형식으로 수정해 보기 -> Kc-DeBERTa는 tensorflow로 적용 불가


2024/08/20
AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ 최적의 파라미터 도출과 평가지표 산출. 하루종일 돌렸으나 안끝나서 켜놓고 갔으나, 컴퓨터 꺼짐


2024/08/19
AI 뉴스에 따른 호재/악재 예측 (애플 / KF-DeBERTa 모델)
ㄴ Huggingface의 transformers라이브러리와 Trainer클래스를 사용하여 파인튜닝하는 방식으로 진행. 최적의 파라미터 도출과 평가지표 산출 작업 필요

AI 과거지표에 따른 회귀분석을 통한 주가 예측 (애플 / Exponential Smoothing 모델)
ㄴ Exponential Smoothing을 활용한 시계열 분석 사용법을 공부하고, 애플 주가 데이터를 적용하여 코드 작성 진행


2024/08/16
AI 뉴스에 따른 호재/악재 예측 (애플 / prophet 모델 - KF-DeBERTa 모델)
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