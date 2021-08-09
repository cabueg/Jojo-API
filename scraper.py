import requests
from bs4 import BeautifulSoup

response = requests.get(
    url= "https://jojo.fandom.com/wiki/Dio_Brando"
)
soup = BeautifulSoup(response.content, 'html.parser')

character_Name = soup.find('h2', attrs={'data-source' : "title"}).string


div = soup.find('div', attrs={'data-source' : "namesake"})
namesake = div.find_all("a", {"class": "extiw"})

print(character_Name)
for a in namesake:
    print(a.string)



# print(namesake)


