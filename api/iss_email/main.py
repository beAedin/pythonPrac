import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time

MY_LAT = 35.871433
MY_LONG = 128.601440

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
def is_over_head():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT+5 and  MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 :
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    # time_now_hour = time_now.hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




while True:
    if is_night() and is_over_head:
        time.sleep(60)
        # Email info
        sendEmail = ""
        recvEmail = ""
        password = ""
        contents = "Look up!! The ISS is above you🌟"

        # Email server info
        smtpName = "smtp.naver.com"
        smtpPort = 587
        msg = MIMEText(contents) #MIMEText(text , _charset = "utf8")

        msg['Subject'] ="HAPPY BIRTHDAY!!"
        msg['From'] = sendEmail
        msg['To'] = recvEmail



        s=smtplib.SMTP( smtpName , smtpPort )
        s.starttls()
        s.login( sendEmail , password )
        s.sendmail( sendEmail, recvEmail, msg.as_string())
        s.close()
