import requests
from bs4 import BeautifulSoup

def get_titles():
    req = requests.get("https://www.nytimes.com")
    soup = BeautifulSoup(req.text, features="html.parser")
    return [el.text for el in soup.find_all(class_="e1voiwgp0")]

def get_filename():
    filename = ""
    while len(filename) == 0:
        filename = input("Filename: ")
    return filename

if __name__ == "__main__":
    titles = get_titles()
    filename = get_filename()
    with open(filename, "w") as open_file:
        open_file.write("\n".join(titles))
