# 2-8 반복문

for x in range(30):
    print(x)

foods = ['된장찌개', '피자', '제육볶음']
for x in range(3):
    print(foods[x])
for x in foods:
    print(x)


information = {'고향': '수원', '취미': '영화관람'}
for x, y in information.items():
    print(x)
    print(y)

# 2-9 집합(set) - 합집합, 차집합, 교집합 (반복제거)

foods = ['된장찌개', '피자', '제육볶음']
foods_set1 = set(foods)
foods_set2 = set(['된장찌개', '피자', '제육볶음'])
print(foods_set1)
print(foods_set2)
# 프린트 할 때마다 값의 순서가 바뀐다. 집합은 값의 순서를 보장하지 않는다.

# 2-10

foods = ['된장찌개', '피자', '제육볶음', '된장찌개']
foods_set = set(foods)
print(foods)
print(foods_set)

menu1 = set(['된장찌개', '피자', '제육볶음'])
menu2 = set(['된장찌개', '떡국', '김밥'])
menu3 = menu1 | menu2  # 합집합
menu4 = menu1 & menu2  # 교집합
menu5 = menu1 - menu2  # 차집합

print(menu3)
print(menu4)
print(menu5)
