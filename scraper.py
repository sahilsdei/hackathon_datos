import requests
from bs4 import BeautifulSoup

# r1 = requests.get("https://artificialintelligence-news.com/")
# coverpage = r1.content
#
# soup1 = BeautifulSoup(coverpage, 'html5lib')
#
# coverpage_news = soup1.find_all('li',attrs={'class':'infinite-post'})
#
# for li in coverpage_news:
#     text=li.find('h2').string
#     link=li.find('a').attrs['href']




r2= requests.get("https://artificialintelligence-news.com/2019/12/09/macquarie-uni-researchers-tech-ai-medical-scribing/")
soup2 = BeautifulSoup(r2.content, 'html5lib')

content_main= soup2.find('div',attrs={'id':'content-main'})

all_text=[]
for row in content_main.find_all('p'):
    if row.string:
        all_text.append(row.string)

print(all_text)
# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html5lib')
#
# quotes = []  # a list to store quotes
#
# table = soup.find('div', attrs={'id': 'all_quotes'})
#
# for row in table.findAll('img'):
#     quote = {}
#     quote['text'] = row.attrs['alt']
#     quote['img'] = row.attrs['src']
#
#     quotes.append(quote)