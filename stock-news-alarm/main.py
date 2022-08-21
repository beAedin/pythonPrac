
import requests
from dotenv import load_dotenv
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os

load_dotenv()
stock_api_key = os.environ.get("stock_api")
NEWS_API_KEY = os.environ.get("news_api")
account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {"function":"TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": stock_api_key}

r = requests.get(STOCK_ENDPOINT, params=stock_params)
data = r.json()["Time Series (Daily)"]

# data_list IS each day information about stock
data_list = [value for (key, value) in data.items()]

# list[0] = yesterday, list[1] = the day before yesterday...
yesterday_data = data_list[0]
yesterday_closing = float(yesterday_data["4. close"])

before_yesterday_data = data_list[1]
before_yesterday_closing = float(before_yesterday_data["4. close"])

difference = round(yesterday_closing - before_yesterday_closing)
up_down: str
if difference > 0 :
    up_down = "🔺"
else:
    up_down = "🔻"

# 그저께 차이/어제 폐장가 * 100
diff_percentage = (difference/yesterday_closing) * 100
print(diff_percentage)

if abs(diff_percentage) > 2 :
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_res = requests.get(NEWS_ENDPOINT, params=news_params)

    articles = news_res.json()["articles"]
    #slice operator
    thr_articles = articles[:3]
    print(thr_articles)


    body = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {i['content']}. \n  {i['description']}" for i in thr_articles]

    client = Client(account_sid, auth_token)
    
    for item in body:
        message = client.messages \
                                .create(
                                    body=body,
                                    from_ = "+14249552394",
                                    to = "+8201065237536"
                                )