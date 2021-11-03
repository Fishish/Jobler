import json

from bs4 import BeautifulSoup
import requests


link = 'https://careers.blizzard.com/global/en/search-results?keywords=Test'
r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')

s = soup.find('script', type='application/ld+json')

# JUST THIS
json = json.loads(s.string)

print(json)