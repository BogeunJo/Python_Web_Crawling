from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(10) # 웹 페이지가 로딩 될 때까지 10초는 기다림
driver.maximize_window() #화면 최대화

# 웹페이지 해당 주소 이동
driver.get("https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0&cat_id=&frm=NVSHATC")

# 상품명
names = driver.find_elements(By.CSS_SELECTOR, ".basicList_link__JLQJf")
for name in names:
    print(name.text)

 