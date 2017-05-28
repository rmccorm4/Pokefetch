# Pokefetch
This is a script I'm working on to further my webscraping skills
## Tools
Python 3

www.serebii.net

## Context
This script currently asks for the pokedex number of the pokemon you'd like
to get information about, then it will get the picture and some related
information such as type, abilities, weaknesses, etc.

I wanted to model the output to be similar to screenfetch and neofetch, two popular scripts to grab system information.

![Alt text](imgs/neofetch.png?raw=true "Neofetch Example")



## How to use it

### Starting steps:

Make sure you have all of the necessary third-party libraries:

Python requests module 

```
pip install requests
```

Python BeautifulSoup module 

```
pip install bs4
```

### Running the script:

```
./pokefetch.sh <pokemon_name>
```

Example below.


## Current progress
This is what I have so far:

![Alt text](imgs/progress.png?raw=true "Pokefetch Example")

## To-do

1) Make sure it works for every single pokemon, including difficult names such as "Mr. Mime" and "Ho-oh"

2) Get higher quality images to output if possible, need to research this more

3) Add a -shiny flag to output the shiny sprite instead of the regular one

4) Scrape more relevant information about the pokemon
