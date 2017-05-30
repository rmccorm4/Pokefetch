"""
Author: Ryan McCormick
File: pokefetch_v2.py
TODO: Use generation (pokedex number range) to get earliest sprite?
"""

""" Standard Libraries """
import sys
import re

""" Third Party Libraries """
from bs4 import BeautifulSoup
import requests

""" Get Pokemon Name """
if len(sys.argv) < 2:
	pokemon = input("Enter the name of the pokemon to look up: ").title()

elif len(sys.argv) == 3:
	pokemon = (sys.argv[1] + " " + sys.argv[2]).title()	

elif len(sys.argv) == 2:
	pokemon = sys.argv[1].title()

else:
	print("You entered too many arguments!")
	sys.exit()

# Fix Special Cases like Mr. Mime and Mime Jr. ###
pokemon = pokemon.replace(' ', '_')

""" Start Webscraping """
url = "http://bulbapedia.bulbagarden.net/wiki/" + pokemon + "_(Pok%C3%A9mon)"
request = requests.get(url)
html = request.content
soup = BeautifulSoup(html, "html.parser")

### CATEGORY ###
# Get full html string
category = str(soup.find(title="Pokémon category").contents[0])
begin = category.find(">")
end = category.find("<", 1)
# Cut it down to just the description
category = category[begin+1 : end]

### POKEDEX ENTRY ###
pokedex = str(soup.find_all(title="List of Pokémon by National Pokédex number")[1].contents[0])
begin = pokedex.find(">")
end = pokedex.find("<", 1)
pokedex = pokedex[begin+1 : end]

### TYPES ###
types = []
for t in soup.find_all(title=re.compile("(type)")):
	if t.b.text != "Unknown":
		types.append(t.b.text)
	else:
		break

### ABILITIES ###
print(soup.find_all("a", href=re.compile("(Ability)"), title=re.compile("(Ability)")))
