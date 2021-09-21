from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)
print(max_value)
print(article_texts[max_index])
print(article_links[max_index])


# all_titles = soup.find_all("storylink")

# for title in all_titles:
#     print(title.get("href"))




# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
    
# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))