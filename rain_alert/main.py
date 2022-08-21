import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')

api_key = os.environ.get('weather_api_key')

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())

client = Client(account_sid, auth_token)
message = client.messages \
                .create(
    body="자니?",
    from_ = "+14249552394",
    to = "+82"
)

print(message.status)