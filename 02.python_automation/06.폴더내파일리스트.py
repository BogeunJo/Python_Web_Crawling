import os

# 현재 폴더 내 모든 파일 출력
file_list=os.listdir("C:/Users/lg/Downloads")
print(file_list)

# 반복문 통해 각 파일의 확장자 확인
for file in file_list:
   name, ext = os.path.splitext(file) #언패킹