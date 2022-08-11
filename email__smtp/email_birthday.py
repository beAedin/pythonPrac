##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import random
from email.mime.text import MIMEText

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# to tuple
tuple = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}



# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_tuple = (now.month, now.day)
print(today_tuple)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
if today_tuple in tuple:
    birthday_person = tuple[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Email info
    sendEmail = ""
    recvEmail = ""
    password = ""

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


