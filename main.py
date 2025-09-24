#  ----------------------- day 45 -------------
from bs4 import BeautifulSoup
# import lxml   # if html.parser is not working 

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())    # give the html code in readble version
# print(soup.li) #will give the first list if html file

#  ---------- for fetching the all of the value like any tag -------
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# ------ for find the anchor tag text & href-------
for tag in all_anchor_tags:
    # print(tag.get_text())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading.string)
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get_text())

#  ------------- for fetch the 1st url -----------
company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

name = soup.select_one(selector="#name")
# print(name)

heading = soup.select(selector=".heading")
# print(heading)


