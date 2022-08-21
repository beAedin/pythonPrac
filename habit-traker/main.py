import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
USERNAME = os.environ.get('pixela_username')
TOKEN = os.environ.get('pixela_token')

pixela_endpoint = "https://pixe.la/v1/users"
coding_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# register...

# res = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# Make Graph
# res = requests.post(url=graph_endpoint, # json=graph_config, headers=headers)
# print(res.text)


# Date Format
now = datetime.now()
date = ''.join(str(now.date()).split('-'))

print(now.strftime("%Y%m%d"))

update_coding_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
pixel_data = {
    "quantity": "1"
}

# res = requests.post(url=coding_endpoint, json=pixel_data, headers=headers)
# print(res.text)


new_pixel_date = {
    "date": date,
    "quantity":"2"
}

# res  = requests.put(url={update_coding_endpoint}, json=new_pixel_date, headers=headers)
# print(res.text)