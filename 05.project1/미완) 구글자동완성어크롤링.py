import requests
import json
import pyautogui

sub_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅋ','ㅌ','ㅍ','ㅎ']
main_keyword = pyautogui.prompt("키워드를 입력하세요")

f = open(f'05.project1/{main_keyword}.txt', 'w', encoding='utf-8')

print(f'검색어 "{main_keyword}" 자동완성어 추출 결과:\n')

for sub in sub_list:
    keyword = main_keyword + ' ' + sub
    response = requests.get(f"https://www.google.com/complete/search?q={keyword}&cp=4&client=gws-wiz&xssi=t&hl=ko&authuser=0&psi=mYmQY_r3GIWF-AacrZnQAw.1670416793876&dpr=1.25")
    origin_data = response.text
    str_data = origin_data.split("_jsonp_10(")[1][:-1]
    dic_data = json.loads(str_data)
    for data in (dic_data['items'][0]):
        f.write(data[0] + '\n')
        print(data[0])

f.close()