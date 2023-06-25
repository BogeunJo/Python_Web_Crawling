# 원본 링크: https://gist.github.com/PyBack/bd7e74104274c98d9bcac414bd4b3ba3

# -*- coding: utf-8 -*-

import os
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# mail_server = smtplib.SMTP('smtp.gmail.com', 587)
# mail_server.starttls()
# pwd = 'toahvxoflsqmtrwm'
# mail_server.login('hyojkim79@gmail.com', pwd)

mail_server = smtplib.SMTP('smtp.naver.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.ehlo()
# mail_server.starttls()
pwd = getpass.getpass('bogeun2882z@')
# pwd = ''
mail_server.login('bogeun000422@naver.com', 'bogeun2882z@')

for i in range(26, 51):
    # target_filename = 'pycharm-community-2021.3.zip.0%.2d' % (i+1)
    target_filename = 'Anaconda3-2021.11-Windows-x86_64.zip.%.3d' % (i+1)
    print(target_filename)


    # 제목, 본문 작성
    msg = MIMEMultipart()
    msg['From'] = 'bogeun000422@naver.com'
    msg['To'] = 'bogeun000422@naver.com'
    msg['Subject'] = target_filename
    msg.attach(MIMEText('test', 'plain'))

    # 파일첨부 (파일 미첨부시 생략가능)
    attachment = open('C:/Users/lg/Desktop/사진/증명사진.jpg' % target_filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename('C:/Users/lg/Desktop/사진/증명사진.jpg' % target_filename)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)

    # 메일 전송
    # mail_server.sendmail("ggtt7@naver.com", "hj.edward.kim@kbfg.com", msg.as_string())
    mail_server.sendmail("bogeun000422@naver.com", msg['To'].split(','), msg.as_string())

mail_server.quit()