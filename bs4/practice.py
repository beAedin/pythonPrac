from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")

yc_web_page = res.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")

a_all = soup.find_all(name="a")
a_texts = []
a_links = []
for i in a_all:
    a_text = i.getText()
    a_texts.append(a_text)
    a_link = i.get("href")
    a_links.append(a_link)


print(a_texts)
print(a_links)

a_first = soup.find(name="a", class_="titlelink")
print(a_first.getText())

# href of a tag
print(a_first.get("href"))

upvote = soup.select_one(selector=".score")
# print(upvote.getText())

# get score from list
all_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote = max(all_upvotes)
# print(max_upvote)
largest_index = all_upvotes.index(max_upvote)

print(a_links[largest_index])