# Pokefetch
This is a script I'm working on to further my webscraping skills
## Tools
Python 3

Python requests module 

```
pip install requests
```

Python BeautifulSoup module 

```
pip install bs4
```

www.serebii.net
## How to use it
This script currently asks for the pokedex number of the pokemon you'd like
to get information about, then it will get the picture and some related
information such as type, abilities, weaknesses, etc.

## To-do
1) Print the information for the pokemon in a screenfetch/neofetch fashion, but replace OS logo with pokemon image and replace cpu information with pokemon name, stats, abilities, etc.

![Alt text](imgs/neofetch.png?raw=true "Neofetch Example")


## Current progress
This is what I have so far:

![Alt text](imgs/progress.png?raw=true "Pokefetch Example")

Things I still want to accomplish:

1) Make sure it works for every single pokemon, including difficult names such as "Mr. Mime" and "Ho-oh"

2) Get higher quality images to output if possible, need to research this more

3) Add a -shiny flag to output the shiny sprite instead of the regular one
