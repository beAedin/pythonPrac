import requests

res = requests.get(url="http://api.open-notify.org/iss-now.json")

# if res.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif res.status_code == 401:
#     raise Exception("You are not authorised to access this data")

# => res.raise_for_status()

data = res.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(longitude)
print(latitude)