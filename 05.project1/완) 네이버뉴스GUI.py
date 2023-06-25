from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import os
from bs4 import BeautifulSoup

UI_PATH= "05.project1\네이버뉴스UI.ui"


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)
        self.pushButton.clicked.connect(self.search_start)
        self.pushButton_2.clicked.connect(self.search_reset)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_4.clicked.connect(self.end)
        
    def search_start(self):
        self.label_3.setText("네이버 뉴스 제목 추출을 시작합니다...")
        QApplication.processEvents()
        keyword = self.lineEdit.text()
        page_num = int(self.lineEdit_2.text())
        for i in range(0, page_num * 10, 10):
            response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
            html = response.text

            soup = BeautifulSoup(html, 'html.parser')
            links = soup.select(".news_tit") # 결과는 리스트
            for link in links:
                title = link.text
                print(title)
                self.textBrowser.append(title)

            self.label_3.setText("네이버 뉴스 제목 추출이 완료되었습니다.")
    
    def search_reset(self):
        
        self.textBrowser.setText("")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_3.setText("리셋되었습니다.")

    def save(self):
        result = self.textBrowser.toPlainText()
        f = open(f'{self.lineEdit.text()}_뉴스제목.txt', 'w', encoding='utf-8')
        f.write(result)
        f.close
        self.label_3.setText(os.getcwd() + f'/{self.lineEdit.text()}_뉴스제목.txt 에 저장되었습니다.')

    def end(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())