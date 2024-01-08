import requests
from bs4 import BeautifulSoup

def get_soup(url):
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

  #select and extract category animals here
def get_categories(url):
  soup = get_soup(url)
  data = {}
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a")
    data[category_name] = category_animals
    
  return data

category_data = get_categories("https://en.wikipedia.org/wiki/Endangered_species")
print(category_data)

