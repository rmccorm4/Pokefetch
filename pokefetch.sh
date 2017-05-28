#!/bin/sh

# Prepend 10 blank lines for nice format
echo > stats.txt
for ((i=0; i<9; i++));
do
	echo >> stats.txt
done

# Get pokemon stats and output to file
/usr/bin/env python3 pokefetch.py $@ >> stats.txt

# Format input for image
POKEMON=$@                # '$@' refers to command line argument
POKEMON=${POKEMON[@]^}    # This converts to Title Case


# Get image and output to file
catimg -w 120 "imgs/$POKEMON.png" > image.txt

# Print image and stats side by side
pr -mts image.txt stats.txt
