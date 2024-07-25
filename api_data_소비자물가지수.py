# 라이브러리 불러오기
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://ecos.bok.or.kr/api/StatisticSearch/"  # 기본 API주소
mykey = ""  # api key 입력
page = "1/100"  # 조회 페이지 설정
class_code = "901Y009"  # 대분류코드 - 분류코드 참조
time_code = "M"  # 주기(년:A, 반년:S, 분기:Q, 월:M, 반월:SM, 일: D)
start_date = "202301"  # 조회시작날짜
end_date = "202406"  #조회끝날짜
end_class_code = "0" # 소분류 10101/?/?/? - 분류코드 참조

# API로 데이터 연결
data = url + mykey + "/xml/kr/" + page + "/" + class_code + "/" + time_code + "/" + start_date + "/" + end_date + "/" + end_class_code

response = requests.get(data)
soup = BeautifulSoup(response.content, "lxml")

# 날짜 데이터
data_time_value = []
data_time = soup.find_all('time')
for i in data_time :
    data_time_value.append(i.text)
data_time_value.reverse()

# 소비자 물가지수
data_value_text = []
data_value = soup.find_all('data_value')
for i in data_value :
    data_value_text.append(i.text)
data_value_text.reverse()

# 데이터 프레임 생성
DF_data = pd.DataFrame(data_value_text, data_time_value, columns=["소비자물가지수"])