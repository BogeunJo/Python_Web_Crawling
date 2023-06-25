import requests
import json
import pyautogui

##네이버 검색 자동완성어 추출
def naver_search_keyword(coreKeyword):
    url = (f'https://ac.search.naver.com/nx/ac?q={coreKeyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_3')
    headers = {'user-agent':('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')}
  
    response = requests.get(url, headers=headers)
    json_string = response.text.split('(')[1].replace(')', '')
    auto_keywords = json.loads(json_string)  # dict로 변환
    print(auto_keywords)

    keywords = []
    for auto_words in auto_keywords['items']:
        for word in auto_words:
            keywords.append(word[0])
    print(f'검색어 "{coreKeyword}" 자동완성어 추출 결과:\n')
    for w in keywords:
        print(w)
     
naver_search_keyword(pyautogui.prompt("검색어를 입력하세요>>>"))