#while 문
# 조건이 False가 될때까지 반복

i=1 # 초기식
while i <= 10:
    print(f'{i}번째 자동화 작업 중')
    i=i+1

while True:
    x=input("종료하려면 exit를 입력하세요 >>>")
    if x=="exit":
        break