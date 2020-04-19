import requests
from bs4 import BeautifulSoup
from csv import writer
import random

history = {}
start = input("Starter: ")
depth = int(input("How deep: "))

link = '/wiki/'+start
for x in range(depth):
    response = requests.get('https://en.wikipedia.org' + link)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [l['href'] for l in list(filter(lambda x: x.has_attr('href') and x['href'].startswith('/wiki/') and not x['href'].startswith('/wiki/Wikipedia'), soup.select('p > a')))]
    link = links[random.randint(0, len(links)-1)]
    print(link)

#Make sure it exists and list > 0




