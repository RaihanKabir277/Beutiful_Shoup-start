# 📰 Hacker News Web Scraper

This project demonstrates **static web scraping** and **live web scraping** using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Requests](https://docs.python-requests.org/).  
It extracts article titles, links, and upvote counts from Hacker News (both the static practice site and the live site), then identifies the **most upvoted article** for both live and static.

---

## 📂 Project Structure
.
- ├── website.html # Sample HTML file for practicing BeautifulSoup
- ├── main.py # Python script for scraping Hacker News
- └── README.md # Documentation
---


---

## 🚀 Features
- Parse local HTML (`website.html`) to practice BeautifulSoup basics:
  - Extract headings, links, and elements by tag, id, and class.
  - Use `.get_text()` and `.get("href")` to fetch data.
- Scrape Hacker News (static and live versions):
  - Collect all article titles and links.
  - Fetch upvote counts for each article.
  - Handle missing upvotes (articles with no points yet).
  - Find and print the **most upvoted article** with its title, link, and score.

---

---
# Sample output (will vary since Hacker News updates in real time):

- Most upvoted article: Show HN: Some cool project
- Number of upvotes: 356 points
- Available at: https://example.com
---

## 🛠️ Requirements
Make sure you have Python installed. Then install dependencies:

```bash
pip install requests beautifulsoup4 lxml

---

