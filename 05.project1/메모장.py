File = open("test.txt", "w", encoding='utf-8') #'w' 는 작성
File.write("이 글은 메모장에 쓰임?ㅋㅋzzzzzzzzzzzzzzzzzz")

# File = open("test.txt", "r", encoding='utf-8') #'r'은 읽기
# lines = File.readlines()
# print(lines)

File.close()