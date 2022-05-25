# 연산자
print('=======산술연산 학습========')
a = 2
b = 3
print(a+b)

# 문자열 연산
print('=======문자열 연산 학습========')
a = '진수'
b = '김'
print(a+b)

# 배열
print('=======배열 학습========')
a_list = ['사과', '배', '감']
print(a_list[2])

a_list.append('수박')
print(a_list)

# 딕셔너리
print('=======딕셔너리 학습========')
a_dict = {'name':'Bob', 'age':27}

print(a_dict)

# 함수 테스트
print('=======함수 학습========')
def sum(a, b):
    print('더하자')
    return a+b

result = sum(1,2)
print(result)

#조건문
print('=======조건문 학습========')
def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')
is_adult(15)
is_adult(25)


#  반복문
print('=======반복문 학습========')
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

for fruit in fruits:
    print(fruit)

count = 0
for aaa in fruits:
    if aaa == '배':
        count += 1

print(count)

# 딕셔너리
print('=======딕셔너리 반복문 학습========')
people = [{'name': 'bob', 'age': 20},
{'name': 'carry', 'age': 38},
{'name': 'john', 'age': 7},
{'name': 'smith', 'age': 17},
{'name': 'ben', 'age': 27}]

for ppp in people:
    print(ppp)

for ppp in people:
    if ppp['age'] > 20:
        print(ppp['name'])
