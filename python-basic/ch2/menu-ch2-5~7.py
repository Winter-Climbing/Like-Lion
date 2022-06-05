import random
# 2-5 변수 선언
lunch = random.choice(['된장찌개', '피자', '제육볶음'])
lunch = '냉장고'
dinner = random.choice(['김밥', '쫄면', '돈까스'])
print(lunch)

# 2-6 key값 가져오기 .get
information = {'고향': '수원', '취미': '영화관람', '좋아하는음식': '제육볶음'}
print(information)
print(information.get('취미'))

myInfo = {'사는 곳': '서울', '특기': '피아노'}
print(myInfo.get('사는 곳'))
print(myInfo.get('특기'))

# 2-7 
information = {'고향': '수원', '취미': '영화관람', '좋아하는 음식': '제육볶음'}  # dictionary
foods = ['된장찌개', '피자', '제육볶음']  # list
print(information.get('취미'))
information['특기'] = '피아노'
information['사는곳'] = '서울'
del information['좋아하는 음식']
print(information)
print(len(information))
information.clear()
print(information)
print(foods[2])  # 앞에서 부터 0 1 2 3 4
print(foods[-1])  # 뒤에서 부터 -1 -2 -3 -4
foods.append('김밥')
print(foods)
del foods[0]
print(foods)
