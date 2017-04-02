import requests
from bs4 import BeautifulSoup
import re
import sys

print(sys.argv)
"""
#request = requests.get(full_url)
#html = request.content

soup = BeautifulSoup(html, "html.parser")
#div = soup.find_all(class_="fooinfo")
nameLine = soup.find(string=re.compile("#"+pokedex_number))
#print(nameLine)
pokemon_name = nameLine[:nameLine.find(" ")]
print(pokemon_name)
"""
#Makes first letter uppercase and the rest lowercase
pokemon = sys.argv[1].title()
request = requests.get("http://serebii.net/pokedex-xy/")
html = request.content
soup = BeautifulSoup(html, "html.parser")
pageInfo = soup.get_text()
#pokedex entries start at index 5000
pokemonIndex = pageInfo.find(pokemon, 5000)
pokedexNumber = pageInfo[pokemonIndex-4:pokemonIndex-1]

begin_url = "http://www.serebii.net/pokedex-xy/"
end_url = ".shtml"
full_url = begin_url + pokedex_number + end_url


baseStatsTotal = soup.find(string=re.compile("Base Stats - Total:"))
baseStats = soup.find_all(class_="fooinfo")
hpLine = str(baseStats[len(baseStats)-21])
attLine = str(baseStats[len(baseStats)-20])
defLine = str(baseStats[len(baseStats)-19])
spattackLine = str(baseStats[len(baseStats)-18])
spdefLine = str(baseStats[len(baseStats)-17])
speedLine = str(baseStats[len(baseStats)-16])

hp = hpLine[hpLine.find(">")+1:hpLine.find("/")-1]
attack = attLine[attLine.find(">")+1:attLine.find("/")-1]
defence = defLine[defLine.find(">")+1:defLine.find("/")-1]
spattack = spattackLine[spattackLine.find(">")+1:spattackLine.find("/")-1]
spdef = spdefLine[spdefLine.find(">")+1:spdefLine.find("/")-1]
speed = speedLine[speedLine.find(">")+1:speedLine.find("/")-1]

print(baseStatsTotal)
print(hp)
print(attack)
print(defence)
print(spattack)
print(spdef)
print(speed)

weaknessList = soup.find_all(class_="footype")

abilitiesIndex = pageInfo.find("Abilities:")
abilities = pageInfo[abilitiesIndex:]
endIndex = abilities.find("\n")
abilities = abilities[:endIndex-1]
#print(abilities)

genderIndex = pageInfo.find("GenderType")
gender = pageInfo[genderIndex:]
endIndex = gender.find("\n")
gender = gender[:endIndex]
#print(gender)

#classificationIndex = pageInfo.find("Classification\n")
#classification = pageInfo[classificationIndex:]
#endIndex = classification.find("\n")
#classification = classification[:endIndex+helperIndex]
#print(classification)

#print(weaknessList)
#for link in weaknessList:
	#print(link.get("src"))

#weaknessList = [weaknessList.attrs("src") for result in weaknessList]
#print(weaknessList)	

base_image_url = "http://www.serebii.net/xy/pokemon/"
full_image_url = base_image_url + pokedex_number + ".png"

response = requests.get(full_image_url)

filename = pokedex_number + ".png"
myfile = open("imgs/"+filename, "wb")
for byte in response:
	myfile.write(byte)
myfile.close()

"""
