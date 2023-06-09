# 이 예시들은 서로 다른 변수를 나타낸다
# 1. apple / Apple   대소문자
# 2. git add. / git add .  띄어쓰기
# 3. message / massage  오타


# 변수, variable
dust = 10
dust = '10'

greeting = 'hello'

# 1
status = True
# 0
status = False

print(dust, greeting, status)


# 리스트
dust_list = [10, 20, 20, 15, 100, 150]
print(dust_list)
print(dust_list[0])

# 딕셔너리
dust_dict = {
    '서울': 100,
    '대전': 50,
    '부산': 10
}

print(dust_dict)
print(dust_dict['서울'])

# 조건

age = 10

if age > 20:
    print('성인입니다')
elif age > 8:
    print('청소년입니다')
else:
    print('어린이입니다')

# 반복

menus = ['짜장면', '국밥', '김밥', '라면', '피자']

n = 0
while n < 2:
    print(menus[n])
    n += 1

for menu in menus:
    print(menu)
