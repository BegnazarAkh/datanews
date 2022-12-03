import requests
from bs4 import BeautifulSoup, NavigableString, Tag

url = "https://stadion.uz/uz/"
page = requests.get(url)
from csv import writer

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div', class_='news_rubrics_main')

with open("news.csv", 'w',  newline='', encoding='utf-8') as f:
    thewriter = writer(f)
    header = ['Link', 'Content', 'Words']
    thewriter.writerow(header)
    for listt in lists:
        urrl = listt.find('a')['href']
        content = listt.find('p')
        words = [str(child).strip(" ") for child in content.children
                 if isinstance(child, NavigableString)]

        newsinfo = [urrl, content.text, words]
        thewriter.writerow(newsinfo)
