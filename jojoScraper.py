import requests
from bs4 import BeautifulSoup
from header import *
from multiprocessing import Pool

part = 3
while(part < 4):
    response = requests.get(
    url= "https://jojo.fandom.com/wiki/Template:Part_"+ str(part) +"_Character_Table"
)
    webPage = BeautifulSoup(response.text, "html.parser")
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

    with Pool(5) as p:
        records = p.map(get_character_info, listofLinks)

    
    part += 1
