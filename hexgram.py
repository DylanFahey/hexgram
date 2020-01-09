#!/usr/bin/env python
'''
hexgram.py

Contains functions for creating, updating and managing puzzle

Methods:
generate()
createdict()
check()
'''

import os
import sys
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

'''
generate
chooses 7 unique letters and then chooses 1 letter to be the center
create word list from dictionary of words which contain center letter and which are constructed exclusively of letters in puzzle
rules for generation:
must include at least 1 vowel (not actually necessary)
'''

# Pick letters for game
'''
pick 7 letters from the dictionary.
It may be a good idea to weight them in the future
random.choices uses replacement
random.sample makes sure letters don't repeat
'''
letters = random.sample(list(alphabet),k=7)

# get the letter in the center
center_letter = letters[0]
print ("center letter is '" + center_letter + "'")

# get the letters on the outside
outside_letters = "".join(letters[1:])

print ("The other letters are " + outside_letters)
# for i in letters[1:]:
#     print(i)

# Create Dictionary
'''
Find all strings that contain letters, with center showing up at least once

Beginning of line + any number of repetitions of letters + one of center letter + any number of repetitions of letters + end of lined

'''
DICTIONARY_PATH = "dictionaries/google10k.txt"
PATTERN_FILE = "puzzlepattern.txt"

regex_pattern = "^[" + center_letter + outside_letters + "]*+[" + center_letter + "]+[" + center_letter + outside_letters + "]*$"
print (regex_pattern)

#TODO write to PATTERN_FILE and use fgrep

#grep_command = "cat " + DICTIONARY_PATH +

# Find words that contain center letters


# Exclude words that contain letters not in puzzle letters

'''
check
checks validity of puzzle

'''
