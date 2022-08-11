

# sendEmail = ""
# recvEmail = ""
# password = ""

# smtpName = "smtp.naver.com" #smtp 서버 주소
# smtpPort = 587 #smtp 포트 번호

# text = "매일 내용"
# msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

# msg['Subject'] ="Title"
# msg['From'] = sendEmail
# msg['To'] = recvEmail
# print(msg.as_string())

# s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
# s.starttls() #TLS 보안 처리
# s.login( sendEmail , password ) #로그인
# s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
# s.close() #smtp 서버 연결을 종료합니다.

import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

now = dt.datetime.now()
day_of_week = now.weekday() # +1



if day_of_week == 1:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
        

    # Email info
    sendEmail = ""
    recvEmail = ""
    password = ""

    # Email server info
    smtpName = "smtp.naver.com"
    smtpPort = 587
    msg = MIMEText(quote) #MIMEText(text , _charset = "utf8")

    msg['Subject'] ="Today's Energizing quote"
    msg['From'] = sendEmail
    msg['To'] = recvEmail



    s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
    s.starttls() #TLS 보안 처리
    s.login( sendEmail , password )
    s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환
    s.close() #smtp 서버 연결을 종료
