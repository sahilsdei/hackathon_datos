import requests
from bs4 import BeautifulSoup
import re

def get_links():
    request1 = requests.get("https://artificialintelligence-news.com/")
    coverpage = request1.content

    soup = BeautifulSoup(coverpage, 'html5lib')

    coverpage_news = soup.find_all('li', attrs={'class': 'infinite-post'})
    links = list()
    for li in coverpage_news:
        text=li.find('h2').string
        link=li.find('a').attrs['href']
        links.append({"link":link,"text":text})
    return links



def get_detail(link):
    raw_link= requests.get(link)
    souped_link = BeautifulSoup(raw_link.content, 'html5lib')

    content_main= souped_link.find('div',attrs={'id':'content-main'})

    all_text=[]
    for row in content_main.find_all('p'):
        if row.string:
            all_text.append(row.string)
    return all_text

def get_quote():
    URL = "http://www.values.com/inspirational-quotes"
    raw_quote = requests.get(URL)

    souped_quote = BeautifulSoup(raw_quote.content, 'html5lib')

    quotes = []

    table = souped_quote.find('div', attrs={'id': 'all_quotes'})

    for row in table.findAll('img'):
        quote = {}
        quote['text'] = row.attrs['alt']
        quote['img'] = row.attrs['src']
        quote['text'] = re.sub(r"[^#]*$", "", quote['text']).replace('#', '')
        quotes.append(quote)
    return quotes