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




