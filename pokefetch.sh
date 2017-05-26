#!/bin/sh
/usr/bin/env python3 pokefetch.py $@
catimg -w 120 "imgs/Pikachu.png"
# Try this out:
# catimg -w 120 "imgs/Pikachu.png" | column -t

#Use catimg to print pixel art, width of 200 pixels is good balance of size/quality

