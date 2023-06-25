from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
driver.get("https://m.naver.com/")

# 탭 버튼 클릭
driver.find_element(By.CSS_SELECTOR, ".sch_ico_aside").click()

# 로그인하세요 버튼 클릭
driver.find_element(By.CSS_SELECTOR, ".ss_name").click()

# 아이디 입력창
id= driver.find_element(By.CSS_SELECTOR, ".input_text")
id.click()
pyperclip.copy("bogeun000422")
pyautogui.hotkey("ctrl", "v" )
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, ".input_password")
pw.click()
pyperclip.copy("bogeun2882z@")
pyautogui.hotkey("ctrl", "v" )
time.sleep(1)

# # 로그인 버튼
driver.find_element(By.CSS_SELECTOR, ".btn_check").click()

# X 버튼
driver.find_element(By.CSS_SELECTOR, ".ah_link_landing.ah_close").click()

# 검색창
driver.find_element(By.CSS_SELECTOR, "#MM_SEARCH_FAKE").click()

# 검색어 입력
driver.find_element(By.CSS_SELECTOR, "#query").click()
pyperclip.copy("경제적자유")
pyautogui.hotkey("ctrl", "v" )
time.sleep(2)

# 검색 버튼
driver.find_element(By.CSS_SELECTOR, "#sch_w > div > form > button > span.sch_ico_mask").click()

# VIEW 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#_sch_tab > div.sch_tab_inner > div > div > ul > li:nth-child(2) > a > span").click()
time.sleep(2)

# 옵션 클릭
driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_filter._search_option_simple_wrap > div > div.option_filter > a").click()

# 블로그 클릭
driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_sort._search_option_detail_wrap > ul > li:nth-child(1) > div > div > a:nth-child(2)").click()
time.sleep(2)

# 옵션 클릭 2
driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_filter._search_option_simple_wrap > div > div.option_filter > a").click()

# 최신순 클릭
driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_sort._search_option_detail_wrap > ul > li.bx.lineup > div > div > a:nth-child(2)").click()

n = 5
count = 0
index = 0
i = 1

#반복
while count < n :

    # 새 탭에서 링크 열기
    target = driver.find_element(By.CSS_SELECTOR, f"#addParemt > li:nth-child({i}) > div > div.total_sub > span > span > span.elss.etc_dsc_inner > a")
    target.send_keys(Keys.CONTROL +"\n")

    # 새 탭으로 이동
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    try:
        # 이웃추가 클릭
        driver.find_element(By.CSS_SELECTOR, "#root > div.blog_cover__Il6gZ > div > div.btn_area__OtwBw > div:nth-child(1) > button").click() 

        # 서로이웃추가 클릭
        driver.find_element(By.CSS_SELECTOR, "#bothBuddyRadio").click()

        # 텍스트상자 내용 지우기
        driver.find_element(By.CSS_SELECTOR, ".textarea_t1").clear()

        # 텍스트상자 내용 입력
        tb = driver.find_element(By.CSS_SELECTOR, ".textarea_t1")
        tb.click()
        pyperclip.copy("경제적 자유에 관심있는 청년입니다. 소통하고 싶어 서로이웃 추가 요청 드립니다~")
        pyautogui.hotkey("ctrl", "v" )
        time.sleep(1)

        # 확인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, ".btn_ok").click() 
        time.sleep(2)
        count = count + 1
        
    except:
        pass

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    index = index + 1
    i = i + 1
