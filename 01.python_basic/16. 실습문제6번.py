from random import randrange
number=randrange(1,101)
tries=1

print("컴퓨터가 숫자를 골랐습니다.")
while True:
   x=int(input("(1~100) 숫자를 맞춰 보세요 >>>"))
   if x==number:
      print("정답입니다!")
      print("총시도 횟수", tries)
      break
   else:
      tries=tries+1
      if x<number:
         print("up 입니다.")
      if x>number:
         print("down 입니다.")
        