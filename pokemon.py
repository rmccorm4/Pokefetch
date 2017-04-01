import requests
from bs4 import BeautifulSoup
import re

begin_url = "http://www.serebii.net/pokedex-xy/"
pokedex_number = input("Enter pokedex number XXX, eg: pikachu would be 025: ")
end_url = ".shtml"
full_url = begin_url + pokedex_number + end_url

request = requests.get(full_url)
html = request.content

soup = BeautifulSoup(html, "html.parser")
#div = soup.find_all(class_="fooinfo")
nameLine = soup.find(string=re.compile("#"+pokedex_number))
#print(nameLine)
pokemon_name = nameLine[:nameLine.find(" ")]
print(pokemon_name)

baseStatsTotal = soup.find(string=re.compile("Base Stats - Total:"))
print(baseStatsTotal)

baseStats = soup.find_all(class_="fooinfo")
speedLine = baseStats[len(baseStats)-16]
speed = speedLine[speedLine.find(">")+1:speedLine.find("/")-1]

base_image_url = "http://www.serebii.net/xy/pokemon/"
full_image_url = base_image_url + pokedex_number + ".png"

response = requests.get(full_image_url)

filename = pokedex_number + ".png"
myfile = open("imgs/"+filename, "wb")
for byte in response:
	myfile.write(byte)
myfile.close()
