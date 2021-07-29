from bs4 import BeautifulSoup
from urllib.request import urlopen

soup=urlopen('https://en.wikipedia.org/wiki/list_of_countries_by_foreign-exchange_reverse_(excluding_gold)').read()
print(type(soup))
print(soup.pretiffy{}[])