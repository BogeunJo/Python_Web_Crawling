import requests
from bs4 import BeautifulSoup

response =requests.get("https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# soup.select_one("선택자")
# soup.select("선택자")

results = soup.select("dt > a")
for result in results:
    title = result.text
    link = result.attrs['href']
    print(title, link)