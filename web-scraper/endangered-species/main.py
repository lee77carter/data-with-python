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

def get_animal(url):
    soup = get_soup(url)
    table = soup.find("table", {"class": "infobox biota"})
    if not table:
      return "No class found."
    rows = table.find_all("tr")
    for row in rows:
      if "Class:" in row.get_text():
        animal_class = row.find("a").contents[0]
    return animal_class

category_data = get_categories("https://en.wikipedia.org/wiki/Endangered_species")

animal_class = get_animal("https://en.wikipedia.org/wiki/Honey_badger")

print(animal_class)

