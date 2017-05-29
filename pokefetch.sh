#!/bin/sh

# Make output directory if it doesn't already exist
mkdir -p output

# Prepend 10 blank lines for nice format
echo > output/stats.txt
for ((i=0; i<9; i++));
do
	echo >> output/stats.txt
done

# Get pokemon stats and output to file
/usr/bin/env python3 pokefetch.py $@ >> output/stats.txt

# Format input for image
POKEMON=$@                # '$@' refers to command line argument
POKEMON=${POKEMON[@]^}    # This converts to Title Case
if [ $POKEMON == "Ho-oh" ] ; then
	POKEMON="Ho-Oh"
elif [ $POKEMON == "Mr. Mime" ] ; then
	POKEMON="Mr.Mime"
fi

# Get image and output to file
catimg -w 120 "imgs/$POKEMON.png" > output/image.txt

# Print image and stats side by side
pr -mts output/image.txt output/stats.txt
