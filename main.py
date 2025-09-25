#  ----------------------- day 45 -------------
from bs4 import BeautifulSoup
# # import lxml   # if html.parser is not working 

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup)
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())    # give the html code in readble version
# # print(soup.li) #will give the first list if html file

# #  ---------- for fetching the all of the value like any tag -------
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # ------ for find the anchor tag text & href-------
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     # print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# # print(heading.string)
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get_text())

# #  ------------- for fetch the 1st url -----------
# company_url = soup.select_one(selector="p a")
# # print(company_url.get("href"))

# name = soup.select_one(selector="#name")
# # print(name)

# heading = soup.select(selector=".heading")
# # print(heading)

# ------------------------Static Scrapting live website starts here ----------------
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# all_anchor_tags = soup.find_all(name="a", class_ ="storylink")
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     pass
#  -------- find 1st heading from the website -------------------

# article_tag = soup.find(name="a", class_ ="storylink")
# article_text = article_tag.get_text()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_ ="score").get_text()

# ----------- find all heading and anchor tag and upvoting from the website ----------------

articles = soup.find_all(name="a", class_ ="storylink")
article_text = []
article_link = []
for tag in articles:
    article_text.append(tag.get_text())
    article_link.append(tag.get("href"))

article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_ ="score")]

# print(article_text)
# print(article_link)
# print(max(article_upvote))

# max_score = max(article_upvote)
# max_index = article_upvote.index(max_score)
max_index = article_upvote.index(max(article_upvote))
print(article_text[max_index])
print(article_link[max_index])
# print(max_score)
print(article_upvote[max_index])

# first_item = article_upvote[0]
# print(first_item)


# ----------------- live scrapting added here -----------

from bs4 import BeautifulSoup
import requests

# Live Website (will change over time)
response = requests.get("https://news.ycombinator.com/")
# Static practice website (below code will not work):
# response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

# Finding the upvotes
# If all articles on the page have upvotes, this will work:
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# However, some submissions may not have any upvotes yet.
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
subtexts = soup.findAll(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)

