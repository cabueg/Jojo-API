import requests, json
from bs4 import BeautifulSoup

#returns a string of character name
def find_character_name(soup):
    return soup.find('h2', attrs={'data-source' : "title"}).string


#returns stand name or None if applicable
def find_character_stand(soup):
    try:
        stand = soup.find('div', attrs={'data-source' : "stand"})
        return stand.find("a").string
        
    except AttributeError:
        return None

def find_stand_namesake(soup):
    div = soup.find('div', attrs={'data-source' : "namesake"})
    namesake = div.find("a", {"class": "extiw"}).string
    return namesake 

#returns a list of namesakes or none if applicable
def find_character_namesakes(soup):
    try:
        listOfNamesakes = []

        if(find_character_stand(soup) is not None):
            div = soup.find('div', attrs={'data-source' : "stand"})
            stand = div.find("a")
            response = requests.get(
                url= "https://jojo.fandom.com" + stand['href'])
            stand_Page = BeautifulSoup(response.text, "html.parser")
            stand_Namesake = find_stand_namesake(stand_Page)
            listOfNamesakes.append(stand_Namesake)


        div = soup.find('div', attrs={'data-source' : "namesake"})
        namesake = div.find_all("a", {"class": "extiw"})
        
        for a in namesake:
            listOfNamesakes.append(a.string)

        return listOfNamesakes

    except AttributeError:
        if listOfNamesakes: return listOfNamesakes
        else: return []

    
def get_character_info(link_to_character_page):
    response = requests.get(
        url= "https://jojo.fandom.com" + link_to_character_page)
    character_Page = BeautifulSoup(response.text, "html.parser")
    character_Name = find_character_name(character_Page)
    character_Namesake = find_character_namesakes(character_Page)
    character_Stand = find_character_stand(character_Page)

    character_json = {
        "name": character_Name,
        "stand": character_Stand,
        "namesake": character_Namesake
    }

    character_json = json.dumps(character_json)


    #insert post request here
    
    



