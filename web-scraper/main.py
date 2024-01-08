import requests
from bs4 import BeautifulSoup

honey_badger = requests.get("https://en.wikipedia.org/wiki/Honey_badger")
honey_badger.raise_for_status()
honey_badger_html = honey_badger.text.encode("utf-8")
honey_badger_soup = BeautifulSoup(honey_badger_html, 'html.parser')

