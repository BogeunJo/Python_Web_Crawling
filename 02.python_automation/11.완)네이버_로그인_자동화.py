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
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 아이디 입력창
id= driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("bogeun000422")
pyautogui.hotkey("ctrl", "v" )
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("bogeun2882z@")
pyautogui.hotkey("ctrl", "v" )
time.sleep(2)

# 로그인 버튼
login_btn=driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()

# 메일함 이동
driver.get("https://mail.naver.com/")
time.sleep(2)

# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(2)

# 받는 사람
driver.find_element(By.CSS_SELECTOR, "#user_input_1").send_keys("bogeun000422@naver.com")
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR,"#subject_title").send_keys("셀레니움으로 보낸 메일")
time.sleep(2)

# iframe 안으로 들어가기
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe"))

# 본문
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("자동화 코드로 메일 자동 발송하기")

# iframe 밖으로 나오기
driver.switch_to.default_content()

# 보내기 버튼
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()