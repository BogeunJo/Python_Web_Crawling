from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os
import time
import pyautogui
import pyperclip


UI_PATH= "06.project2/네이버 이웃 추가 프로그램.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)
        self.start_btn.clicked.connect(self.search_start)
        self.reset_btn.clicked.connect(self.search_reset)
        self.close_btn.clicked.connect(self.end)

    def search_start(self):
        self.status.setText("서로이웃 추가를 시작합니다...")
        QApplication.processEvents()

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
        pyperclip.copy(self.id.text())
        pyautogui.hotkey("ctrl", "v" )
        time.sleep(1)

        # 비밀번호 입력창
        pw = driver.find_element(By.CSS_SELECTOR, ".input_password")
        pw.click()
        pyperclip.copy(self.pw.text())
        pyautogui.hotkey("ctrl", "v" )
        time.sleep(1)

        # 로그인 버튼
        driver.find_element(By.CSS_SELECTOR, ".btn_check").click()
        time.sleep(1)

        # 로그인 완료
        # 정렬: 블로그, 최신순
        # 검색어 입력
        main_keyword = self.keyword.text()
        search_url = f"https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_opt&query={main_keyword}&nso=so%3Add%2Cp%3A"

        driver.get(search_url)
        time.sleep(1)
            
        n = int(self.spinBox.value()) # 총 이웃 신청 개수
        count = 0 # 현재 이웃 신청 개수
        index = 0 # 현재 블로그 글 번호

        while count < n :
            ids = driver.find_elements(By.CSS_SELECTOR, ".sub_txt.sub_name")

            # 현재 블로그 글 번호에 맞는 아이디 찾기
            id = ids[index]

            # 새 창으로 열기
            id.send_keys(Keys.CONTROL + '\n')
            time.sleep(1)

            # 새 창으로 드라이버 전환
            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[1])
            time.sleep(2)

            try:
                # 이웃추가 클릭
                driver.find_element(By.CSS_SELECTOR, "#root > div.blog_cover__Il6gZ > div > div.btn_area__OtwBw > div:nth-child(1) > button").click() 

                # 서로이웃추가 클릭
                driver.find_element(By.CSS_SELECTOR, "#bothBuddyRadio").click()

                # 텍스트상자 내용 지우고 입력
                input_message = self.plainTextEdit.text()
                textarea= driver.find_element(By.CSS_SELECTOR, ".textarea_t1")
                textarea.send_keys(Keys.CONTROL, 'a')
                time.sleep(1)
                textarea.send_keys(Keys.DELETE)
                time.sleep(1)
                textarea.send_keys(input_message)
                time.sleep(1)

                # 확인 버튼 클릭
                driver.find_element(By.CSS_SELECTOR, ".btn_ok").click()
                count = count + 1 # 현재 이웃 신청 개수 증가
                time.sleep(2)
            except:
                pass

            # 새 창 닫기
            driver.close()
            
            # 기존 창으로 드라이버 전환
            driver.switch_to.window(all_windows[0])
            index = index + 1 # 현재 블로그 글 번호 증가
            
        self.status.setText("자동완성 키워드 추출이 완료되었습니다.")

    def search_reset(self):
            self.plainTextEdit.clear()
            self.id.setText("")
            self.pw.setText("")
            self.keyword.setText("")
            self.max.clear()
            self.status.setText("리셋되었습니다.")

    def end(self):
        sys.exit()



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())