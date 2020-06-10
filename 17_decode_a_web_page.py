import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.nytimes.com")
soup = BeautifulSoup(req.text, features="html.parser")

for el in soup.find_all(class_="e1voiwgp0"):
    print(el.text)
