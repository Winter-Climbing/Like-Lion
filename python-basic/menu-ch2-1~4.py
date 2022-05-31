# 파이썬은 기본으로 제공해주는 수식과 그렇지 않은 수식이 있다
# 제공해주지 않은 수식의 경우 import를 써야 한다.
import random
import time

# DRY
# Don;t Repeat Yourself

# 파이썬은 들여쓰기가 중요하다!!!
for x in range(30):
    print(random.choice(['된장찌개', '피자', '치킨', '떡볶이', '감자튀김']))
    print('이 문장도 반복되나')

# 무한루프다. time.sleep은 1초 쉬고 코드를 실행해라는 뜻.
while True:
    print(random.choice(['된장찌개', '피자', '치킨', '떡볶이', '감자튀김']))
    print('이 문장도 반복되나')
    time.sleep(1)
    break
