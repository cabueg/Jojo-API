import requests
from bs4 import BeautifulSoup
from header import find_character_name, find_character_namesakes, find_character_stand
import time

#part = 1 for now since going through 
part = 1


starttime = time.time()
while(part < 6):
    response = requests.get(
    url= "https://jojo.fandom.com/wiki/Template:Part_"+ str(part) +"_Character_Table"
)
    webPage = BeautifulSoup(response.content, "html.parser")
    characterTable = webPage.find("table")

    #created empty list run a for loop checking for all links in table
    listofLinks = []
    for i in characterTable.find_all("a", href=True):
        #checks if element is a picture(starts with https) or if it already exists in list
        if i['href'][0] == "h" or i['href'] in listofLinks:
            pass
        #otherwise adds to list
        else:
            listofLinks.append(i['href'])
    #pop the first element of the list because that is the part name (eg. Phantom Blood, Battle Tendancy)
    listofLinks.pop(0)

    for i in listofLinks:
        response = requests.get(
        url= "https://jojo.fandom.com" + i)

        character_Page = BeautifulSoup(response.content, "html.parser")
        character_Name = find_character_name(character_Page)
        character_Namesake = find_character_namesakes(character_Page)
        character_Stand = find_character_stand(character_Page)

        print(character_Name)
        print(character_Namesake)
        print(character_Stand)
        print()
    
    part += 1

print('That took {} seconds'.format(time.time() - starttime))