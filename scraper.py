import requests
from bs4 import BeautifulSoup

response = requests.get(
    url= "https://jojo.fandom.com/wiki/Will_Anthonio_Zeppeli"
)
soup = BeautifulSoup(response.content, 'html.parser')

character_Name = soup.find(id="firstHeading")

div = soup.find_all("a", {"class": "extiw"})

print(div)

