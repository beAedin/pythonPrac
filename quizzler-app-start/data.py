import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
# res = requests.get("https://opentdb.com/api.php", params=parameters)

URL = "https://opentdb.com/api.php?amount=10&type=boolean"


res = requests.get(url=URL)
res.raise_for_status
data = res.json()

question_data = data["results"]