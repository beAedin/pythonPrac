import requests
from bs4 import BeautifulSoup
URL = "https://www.amazon.com/dp/B0B9H71ZSG/ref=twister_B09BQGZFT1?th=1&psc=1"

res= requests.get("http://www.example.com/", headers={"Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})

web_site = res.text
soup = BeautifulSoup(web_site, "lxml")
print(soup.prettify())
price_span = soup.find_all(name="span", class_="a-offscreen")
print(price_span)