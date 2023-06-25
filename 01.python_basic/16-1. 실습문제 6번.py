import random

print("컴퓨터가 숫자를 골랐습니다.")
answer=random.randint(1,100)
try_count=1

while True:
    x=int(input("(1~100) 숫자를 맞춰 보세요 >>>"))

    if x==answer:
        print("정답입니다!")
        print("총시도 횟수", try_count)
        break
    elif x>answer:
        print("down 입니다.")
    else:
        print("up 입니다.")

    try_count = try_count + 1
