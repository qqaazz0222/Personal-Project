# 라이브러리 import
import requests
import pprint
import json

# url 입력
url = 'https://apis.data.go.kr/6260000/BusanDischrgStusService/getTblDischrgStusInfo?serviceKey=qI4qMLNr02e3nPVuyyOkvSevRADw624d%2F3%2FLswq4pBy6%2BuN%2Fl%2Fg4eWIhffSCZptd3ww3IHp1G3HJPbDMRVl%2B7w%3D%3D&pageNo=1&numOfRows=20&loc=서면역&resultType=json'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text