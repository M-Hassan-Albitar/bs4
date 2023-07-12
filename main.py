from bs4 import BeautifulSoup
import requests

website_url = "https://news.ycombinator.com/news"

response = requests.get(website_url)

website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

articles = soup.select(".athing td.title span.titleline > a")
articles_titles_list = []
articles_links_list = []
for article in articles:
    articles_titles_list.append(article.get_text())
    articles_links_list.append(article.get("href"))

upvote_int_list = [int(score.get_text().split()[0]) for score in soup.select("td.subtext")]

high_vote_index = upvote_int_list.index(max(upvote_int_list))
high_title = articles_titles_list[high_vote_index]
high_link = articles_links_list[high_vote_index]
high_vote = upvote_int_list[high_vote_index]

print(high_title)
print(high_link)
print(high_vote)

# print(len(articles_titles_list))
# print(len(articles_links_list))
# print(len(upvote_int_list))

# with open("./website.html", "r", encoding="utf-8") as html_file:
#     data = html_file.read()
#
#
# soup = BeautifulSoup(data, "html.parser")
#
# print(soup)
