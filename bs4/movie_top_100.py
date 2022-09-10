from this import d
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


res = requests.get(URL)
content = res.text

soup = BeautifulSoup(content, "html.parser")
title_all = soup.find_all(class_="title", name="h3", encoding='UTF-8')


title_list = []
# for i in title_all:
#     title_list.append(i.getText())

title_list = [title.getText() for title in title_all]
# title_list.reverse()
# title_list[::-1]
movies = title_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")