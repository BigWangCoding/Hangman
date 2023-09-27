import requests
from bs4 import BeautifulSoup
import json

url = requests.get("https://www.phrases.org.uk/meanings/phrases-and-sayings-list.html").text

soup = BeautifulSoup(url, "html5lib")

find_tag_conent = soup.find("div", class_="content")

find_phrases = find_tag_conent.find_all("p", class_="phrase-list")

listOfPhrase = {}
c = 0
for i in find_phrases:
    phrase = i.find("a")
    try:
        listOfPhrase[c] = phrase.text.strip()
        c += 1
    except UnicodeEncodeError:
        continue
with open("database.json", "w") as database:
    json.dump(listOfPhrase, database, indent=1)



