import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'

res = requests.get(URL)

# print(res.text)

data = BeautifulSoup(res.text, 'html.parser')

selector = '#KOSPI_now'
kospi = data.select_one(selector)

print(kospi)


#######################################

URL2 = 'https://finance.naver.com/sise/'

# requests에 속한 get 메소드로 URL2의 주소 정보를 가져온다
res2 = requests.get(URL2)
# 거기서 .text로 텍스트 데이터만 가져오고 그것을 BeautifulSoup()에 넣는다. html.parser를 입력해 이게 html 기반 데이터라는 것을 명시해 준다.
data2 = BeautifulSoup(res2.text, 'html.parser')

# 개발자 도구에서 kosdaq을 나타내는 이미지를 콘솔 기능을 이용해 클릭하여 selector 부분을 copy 하여 selector2 변수에 저장한다.
selector2 = '#KOSDAQ_now'
# 파싱된 data2의 select_one 메소드를 사용해 selector2가 지정한 데이터를 kosdaq 변수에 저장한다.
kosdaq = data2.select_one(selector2)

print(kosdaq)
