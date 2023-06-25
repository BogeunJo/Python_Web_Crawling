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


UI_PATH= "06.project2/네이버 이웃 추가 프로그램.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        self.start_btn.clicked.connect(self.main)
        self.reset_btn.clicked.connect(self.reset)
        self.close_btn.clicked.connect(self.close)

    def main(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        input_keyword = self.keyword.text()
        input_max = self.max.value()
        input_message = self.message.toPlainText()

        # validation check (유효성 검사)
        if input_id =="" or input_pw =="" or input_keyword=="" or input_message =="":
            self.status.setText("빈칸을 채워주세요")
            return 0 # 함수 종료시킴

        self.status.setText("로그인 진행중...")
        QApplication.processEvents()

        driver = self.login(input_id, input_pw)

        if driver == 0:
            self.status.setText("로그인 실패, 아이디 비밀번호 확인")
            return 0 # 함수 종료시킴
        else:
            self.status.setText("로그인 성공")
            QApplication.processEvents()
            time.sleep(1)
            self.status.setText("자동화 진행중...")
            QApplication.processEvents()
            self.start(driver, input_keyword, input_max, input_message)
            self.status.setText("자동화 완료!")


    def login(self, input_id, input_pw):

        # 브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)

        # 불필요한 에러 메시지 없애기
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.implicitly_wait(3) # 웹 페이지가 로딩 될 때까지 3초는 기다림
        driver.maximize_window() #화면 최대화

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

    def start(self, driver, input_keyword, input_max, input_message):
        
        search_url = f"https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_opt&query={input_keyword}&nso=so%3Add%2Cp%3A"

        driver.get(search_url)
        time.sleep(1)
            
        n = input_max # 총 이웃 신청 개수
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

    def reset(self):
            self.message.clear()
            self.id.setText("")
            self.pw.setText("")
            self.keyword.setText("")
            self.max.clear()
            self.status.setText("리셋되었습니다.")

    def close(self):
        sys.exit()



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())