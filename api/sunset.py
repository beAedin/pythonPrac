import requests
MY_LAT = 35.871433
MY_LONG = 128.601440

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted":0}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters, verify=False,
)

#response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunrise = sunrise.split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"]
print(sunrise)