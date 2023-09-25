import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.phrases.org.uk/meanings/phrases-and-sayings-list.html").text

soup = BeautifulSoup(url, "html5lib")

find_tag_conent = soup.find("div", class_="content")

find_phrases = find_tag_conent.find_all("p", class_="phrase-list")

with open("Phrases.csv", "w") as file:
    for i in find_phrases:
        phrase = i.find("a")
        try:
            file.write((phrase.text.strip() + "\n"))
        except UnicodeEncodeError:
            continue
