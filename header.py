import requests
from bs4 import BeautifulSoup

response = requests.get(
    url= "https://jojo.fandom.com/wiki/Jonathan_Joestar"
)
soup = BeautifulSoup(response.content, 'html.parser')
#returns a string of character name
def find_character_name(soup):
    return soup.find('h2', attrs={'data-source' : "title"}).string

#returns a list of namesakes or none if applicable
def find_character_namesakes(soup):
    try:
        div = soup.find('div', attrs={'data-source' : "namesake"})
        namesake = div.find_all("a", {"class": "extiw"})

        #list comprehension.Equivalent to 
        #
        #listOfNamesakes = []
        #for a in namesake:
        #   listOfNamesakes.append(a.string)
        #
        #saves a lot of space
        listOfNamesakes = [a.string for a in namesake]
        return listOfNamesakes

    except AttributeError:
        return []

#returns stand name or None if applicable
def find_character_stand(soup):
    try:
        stand = soup.find('div', attrs={'data-source' : "stand"})
        return stand.find("a").string
        
    except AttributeError:
        return None

    

    

# print(namesake)


