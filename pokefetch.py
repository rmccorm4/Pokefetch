from bs4 import BeautifulSoup
import requests
import sys
import re

######## Get Pokemon Name ########
if len(sys.argv) < 2:
	pokemon = input("Enter the name of the pokemon to look up: ").title()

# Two Word Names Like Mime Jr.
elif len(sys.argv) == 3:
	pokemon = (sys.argv[1] + " " + sys.argv[2]).title()

else:
	pokemon = sys.argv[1].title()

if pokemon == "Mr. Mime":
	pokemon = "Mr.Mime" #serebii listed this way

elif pokemon == "Ho-Oh":
	pokemon = "Ho-oh" #serebii listed this way

######## Get Pokedex Entry Number  ########
begin_url = "http://serebii.net/pokedex-xy/"
request1 = requests.get(begin_url)
html1 = request1.content
soup1 = BeautifulSoup(html1, "html.parser")
page_info1 = soup1.get_text()
# Pokedex Entries Start At Index 5000
pokemon_index = page_info1.find(pokemon, 5000)

if pokemon_index == -1:
	print("You didn't enter a valid pokemon!")
	sys.exit()

pokedex_number = page_info1[pokemon_index-4 : pokemon_index-1]

######## Get Pokemon Info ########
full_url = begin_url + pokedex_number + ".shtml"
request2 = requests.get(full_url)
html2 = request2.content
soup2 = BeautifulSoup(html2, "html.parser")
page_info2 = soup2.get_text()

######## Get Stats ########
base_total = soup2.find(string=re.compile("Base Stats - Total:"))
# Only want everything after Total
base_total = base_total[base_total.find("Total"):]
base_stats = soup2.find_all(class_="fooinfo")

hp = str(base_stats[len(base_stats)-21])
attack = str(base_stats[len(base_stats)-20])
defence = str(base_stats[len(base_stats)-19])
spec_attack = str(base_stats[len(base_stats)-18])
spec_defence = str(base_stats[len(base_stats)-17])
speed = str(base_stats[len(base_stats)-16])

hp = hp[hp.find(">")+1 : hp.find("/")-1]
attack = attack[attack.find(">")+1 : attack.find("/")-1]
defence = defence[defence.find(">")+1 : defence.find("/")-1]
spec_attack = spec_attack[spec_attack.find(">")+1 : spec_attack.find("/")-1]
spec_defence = spec_defence[spec_defence.find(">")+1 : spec_defence.find("/")-1]
speed = speed[speed.find(">")+1:speed.find("/")-1]

######## Get Abilities ########
abilities_index = page_info2.find("Abilities:")
abilities = page_info2[abilities_index:]
end_index = abilities.find("\n")
abilities = abilities[:end_index-1]

######## Get Gender ########
gender_index = page_info2.find("GenderType")
gender = page_info2[gender_index:]
end_index = gender.find("\n")
gender = gender[:end_index]
gender = gender[gender.find(" ")+1:]
if "is Genderless" in gender:
	gender = "Genderless"

######## Get Image ########
base_image_url = "http://www.serebii.net/xy/pokemon/"
full_image_url = base_image_url + pokedex_number + ".png"
image_bytes = requests.get(full_image_url)

# Write bytes of image to file
filename = pokemon.title() + ".png"
myfile = open("imgs/"+filename, "wb")
for byte in image_bytes:
    myfile.write(byte)
myfile.close()

######## Print everything out ########
print("Name: ", pokemon)
print("Pokedex Number: ", pokedex_number)
print("Gender Ratio: ", str(gender))
print(abilities)
print("---Base Stats---")
print(base_total)
print("Hp: ", hp)
print("Attack: ", attack)
print("Defence: ", defence)
print("Special Attack: ", spec_attack)
print("Special Defence: ", spec_defence)
print("Speed: ", speed)
