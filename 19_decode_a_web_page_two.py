import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(req.text, features="html.parser")

content = [p.text for p in soup.select(".article__body > p")]
print("\n\n".join(content))
