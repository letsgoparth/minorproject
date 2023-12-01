from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)


soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)

from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'https://www.amazon.co.uk/s?k=dslr+camera&i=black-friday&ref=nb_sb_noss'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)