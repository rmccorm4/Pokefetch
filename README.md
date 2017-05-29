# Pokefetch
This is a script I'm working on to further my webscraping skills
## Tools
Python 3
* Requests
* BeautifulSoup

Bash
* catimg

[Serebii](https://www.serebii.net)

## Context
This script currently asks for the pokedex number of the pokemon you'd like
to get information about, then it will get the picture and some related
information such as type, abilities, weaknesses, etc.

I wanted to model the output to be similar to screenfetch and neofetch, two popular scripts to grab system information.

![Alt text](imgs/neofetch.png?raw=true "Neofetch Example")



## How to use it

### Starting steps:

Make sure you have all of the necessary third-party libraries:

#### Python requests module 

```
pip install requests
```

#### Python BeautifulSoup module 

```
pip install bs4
```


#### catimg

Follow the instructions here:
[https://github.com/posva/catimg](https://github.com/posva/catimg)


### Running the script:

```
./pokefetch.sh <pokemon_name>
```

Example below.


## Current progress
This is what I have so far:

![Alt text](imgs/progress.png?raw=true "Pokefetch Example")

However this requires a full-screen terminal in order to come out nicely.

## To-do

* Make sure it works for every single pokemon, including difficult names such as "Mr. Mime" and "Ho-oh"

* Get higher quality images to output if possible, need to research this more

* Add a -shiny flag to output the shiny sprite instead of the regular one

* Scrape more relevant information about the pokemon

* Make script work for default size terminal as well as full-screen?
