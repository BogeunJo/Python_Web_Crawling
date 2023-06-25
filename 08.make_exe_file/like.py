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
import time
import pyautogui
import pyperclip
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = "네이버공감자동화.ui"
getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(os.path.join(BASE_DIR, UI_PATH), self)

        self.start_btn.clicked.connect(self.main)
        self.close_btn.clicked.connect(self.close)
        self.max_slider.valueChanged.connect(self.max)
    
    def max(self):
        self.max_int.setText(str(self.max_slider.value()))

    def main(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        input_max = self.max_slider.value()

        # validation check (유효성 검사)
        if input_id =="" or input_pw =="" :
            self.status.append("빈칸을 채워주세요")
            return 0 # 함수 종료시킴

        self.status.append("로그인 진행중...")
        QApplication.processEvents()

        driver = self.login(input_id, input_pw)

        if driver == 0:
            self.status.append("로그인 실패, 아이디 비밀번호 확인")
            return 0 # 함수 종료시킴
        else:
            self.status.append("로그인 성공")
            QApplication.processEvents()
            time.sleep(1)
            self.status.append("자동화 진행중...")
            QApplication.processEvents()
            self.start(driver, input_max)
            self.status.append("자동화 완료!")

    def login(self, input_id, input_pw):

        # 브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)

        # 불필요한 에러 메시지 없애기
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.implicitly_wait(3) # 웹 페이지가 로딩 될 때까지 3초는 기다림
        # driver.maximize_window() #화면 최대화

        # 웹페이지 해당 주소 이동
        driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

        # 아이디 입력창
        id= driver.find_element(By.CSS_SELECTOR, "#id")
        id.click()
        pyperclip.copy(input_id)
        pyautogui.hotkey("ctrl", "v" )
        time.sleep(1)

        # 비밀번호 입력창
        pw = driver.find_element(By.CSS_SELECTOR, "#pw")
        pw.click()
        pyperclip.copy(input_pw)
        pyautogui.hotkey("ctrl", "v" )
        time.sleep(1)

        # 로그인 버튼
        driver.find_element(By.CSS_SELECTOR, "#log\.login").click()
        time.sleep(1)

        # 로그인 완료
        # 로그인 성공 시 드라이버 반환
        # 로그인 실패 시 드라입 종료 후 숫자 0 반환

        check = driver.find_elements(By.CSS_SELECTOR, "#minime")

        if len(check) > 0:
            return driver
        else:
            driver.close()
            return 0

    def start(self, driver, input_max):
        
        search_url = "https://m.blog.naver.com/FeedList.naver"

        driver.get(search_url)
        time.sleep(1)
            
        n = input_max # 총 공감 개수
        count = 0 # 현재 공감 신청 개수

        while count < n :
            btns = driver.find_elements(By.CSS_SELECTOR, ".u_likeit_list_btn._button.off")

            if len(btns) == 0:
                break

            # 공감이 안 눌린 첫 번째 게시물 누르기
            btns[0].click()
            # 현재 공감 신청 개수 + 1
            count = count + 1
            time.sleep(1)
                            
        self.status.append("자동완성 키워드 추출이 완료되었습니다.")
    
    def close(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())        

