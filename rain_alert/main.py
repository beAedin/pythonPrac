import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "d64e424ef104c4eb25b52a4586b41ad5"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
