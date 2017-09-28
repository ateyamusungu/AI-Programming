from bs4 import BeautifulSoup

import urllib.request as rq

url = "http://www.strathmore.edu"


data = rq.urlopen(url)
data2 = data.read()

soup = BeautifulSoup(data2)

for link in soup.find_all('a', href=True):
    print(link.get('href'))
