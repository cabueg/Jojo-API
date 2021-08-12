import time 
from multiprocessing import Pool
import requests
from requests.models import StreamConsumedError
from header import find_character_name, find_character_namesakes, find_character_stand
from bs4 import BeautifulSoup

#testing out multiprocessing since jojoScraper.py felt a bit slow running
def get_character_info(x):
    response = requests.get(
        url= "https://jojo.fandom.com" + x)
    character_Page = BeautifulSoup(response.content, "html.parser")
    character_Name = find_character_name(character_Page)
    character_Namesake = find_character_namesakes(character_Page)
    character_Stand = find_character_stand(character_Page)

    print(character_Name)
    print(character_Namesake)
    print(character_Stand)
    print()


startTime = time.time()
response = requests.get(
        url= "https://jojo.fandom.com/wiki/Template:Part_1_Character_Table"
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

with Pool(5) as p:
    records = p.map(get_character_info, listofLinks)


print('That took {} seconds'.format(time.time() - startTime))

# Results: 

# Running the loop on single process, getting names, namesakes, 
# and stands from part one took about 9.5 Seconds 

# Multiprocessing pool took about 2.3 seconds