# 2-11

from random import random
import random

food = random.choice(['된장찌개', '피자', '제육볶음'])

print(food)
if(food == '제육볶음'):
    print('곱배기 주세요')
else:
    print('그냥 주세요')
print('종료')


# 2-12 랜덤으로 오늘 먹을 음식을 골라주는 프로덕트 '오늘 뭐 드실?'

lunch = ['된장찌개', '피자', '제육볶음', '짜장면']
# lunch.append('돈까스')
while True:
    print(lunch)
    item = input('음식을 추가 해주세요 : ')
    if(item == 'q'):
        break
    else:
        lunch.append(item)


# 2-13 '오늘 뭐 드실?' -2

print(lunch)
set_lunch = set(lunch)
