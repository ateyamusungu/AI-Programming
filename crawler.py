from bs4 import BeautifulSoup

import urllib

url = "http://www.strathmore.edu"


data = urllib.urlopen(url).read()

soup = BeautifulSoup(data)

for link in soup.find_all('a', href=True);

print(link.get('href'))
