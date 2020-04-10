import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

item_prices = list(map(lambda i : i.get_text(), soup.select('.price')))
print (item_prices)