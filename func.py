############# 내장함수(책상위에 올려져 있는 함수)
num_list = [1,2,3,4,5]

max_num = max(num_list)

print(max_num)


############### 서랍장에서 꺼내 쓰는 애들
import random

random_number = random.randint(1,46)

print(random_number)


###################### 외부 모듈 (설치가 필요함)
# pip install requests
import requests

######################

menus = ['김밥', '라면', '만두']

menu = random.choice(menus)

print(menu)

numbers = range(1,46)
lucky_list = random.sample(numbers, 6)
# print(lucky_list)


i = 0
while i < 5:
    lotto_num = random.sample(numbers, 6)
    print(lotto_num)
    i = i + 1

for i in range(1,6):
    lotto = random.sample(numbers, 6)
    print(f'{i}번째 당첨번호 {lotto}')


URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1070'

# requests의 get 메소드로 데이터 가져옴
res = requests.get(URL)

# json 으로 변환해서 data 변수에 저장
data = res.json()

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

lotto_numer = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

lucky_number = random.sample(range(1,46), 6)

# print(lotto_numer, lucky_number)

result = set(lotto_numer) & set(lucky_number)

print(result)

