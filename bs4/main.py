from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)

# formatting
print(soup.prettify())

# Find all tags
a_tags = soup.find_all(name='li')

# for tag in a_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")

section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="#name")
headings = soup.select_one(selector=".heading")
print(headings)