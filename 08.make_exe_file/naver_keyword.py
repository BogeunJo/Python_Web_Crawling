import requests
import json
import pyautogui

sub_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅋ','ㅌ','ㅍ','ㅎ']
main_keyword = pyautogui.prompt("키워드를 입력하세요")

# f = open(f'05.project1/{main_keyword}.txt', 'w', encoding='utf-8')

print(f'검색어 "{main_keyword}" 자동완성어 추출 결과:\n')

for sub in sub_list:
    keyword = main_keyword + ' ' + sub
    response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_10")
    origin_data = response.text
    str_data = origin_data.split("_jsonp_10(")[1][:-1]
    dic_data = json.loads(str_data)
    for data in (dic_data['items'][0]):
        # f.write(data[0] + '\n')
        print(data[0])

# f.close()