import os

# 정리할 확장자 리스트
extension_list = ['.jpg', 'jpeg', '.gif', '.png']

# 정리할 폴더
target = "C:/Users/lg/Downloads"

# 만들 폴더
destination = target + "/jpg"

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir(target)

# 반복문을 통해 각 파일의 확장자를 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in extension_list:

        # 파일 이동
        source = os.path.join(target, file)
        os.rename(source, os.path.join(destination, file))
