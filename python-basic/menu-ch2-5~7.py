import random
# 2-5
lunch = random.choice(['된장찌개', '피자', '제육볶음'])
lunch = '냉장고'
dinner = random.choice(['김밥', '쫄면', '돈까스'])
print(lunch)

# 2-6
information = {'고향': '수원', '취미': '영화관람', '좋아하는음식': '제육볶음'}
print(information)
print(information.get('취미'))

myInfo = {'사는 곳': '서울', '특기': '피아노'}
print(myInfo.get('사는 곳'))
print(myInfo.get('특기'))
