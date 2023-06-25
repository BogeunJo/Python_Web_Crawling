import os
import shutil

if not os.path.exists("C:/Users/lg/Desktop/파일자동화"):
    os.mkdir("C:/Users/lg/Desktop/파일자동화")

for root, subdirs, files in os.walk("C:/Users/lg/Desktop/startcoding/02.python_automation/랜덤이미지"):
    for f in files:
        if ".jpg" in f:
            file_to_move = os.path.join(root, f)
            shutil.move(file_to_move,"C:/Users/lg/Desktop/파일자동화" )



# path="C:/Users/lg/Downloads"

# file_list=os.listdir(path)
# file_list_jpg = [file for file in file_list if file.endswith('.jpg')]
# print(file_list_jpg)

# shutil.move(file_list_jpg, "C:/Users/lg/Desktop/startcoding")

# print(file_list)

# print(os.path.splitext(file_list))
# print("확장자: ", os.path.splitext(file_list)[0])