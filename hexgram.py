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

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

'''
generate
chooses 7 unique letters and then chooses 1 letter to be the center
create word list from dictionary of words which contain center letter and which are constructed exclusively of letters in puzzle
rules for generation:
must include at least 1 vowel (not actually necessary)
'''
class GeneratePuzzle():
    # Pick letters for game
    '''
    pick 7 letters from the dictionary.
    It may be a good idea to weight them in the future
    random.choices uses replacement
    random.sample makes sure letters don't repeat
    '''
    letters = random.sample(list(ALPHABET),k=7)

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
    CURRENT_GAME_DICT = "dictionaries/currentgame.txt"
    PATTERN_FILE = "puzzlepattern.txt"

    regex_pattern = "^[" + center_letter + outside_letters + "]*+[" + center_letter + "]+[" + center_letter + outside_letters + "]*$"
    # print (regex_pattern)

    #TODO write to PATTERN_FILE and use fgrep

    # create and run grep to make dictionary for current game
    grep_command = "cat " + DICTIONARY_PATH + "| egrep '" + regex_pattern + "' > " + CURRENT_GAME_DICT

    # run bash command
    os.system(grep_command)


    # mi amigos a mi escuela me llama 'pinche gringo'

    # create text stream and read from game dict
    # with open(CURRENT_GAME_DICT,mode='r') as f:
    #     game_dict = f.readlines()

    '''
    Create 3 sets:
    + Words in game list
    + Words that have been guessed
    + Words that have been guessed correctly
    '''

    word_list = [line.rstrip('\n') for line in open(CURRENT_GAME_DICT)]

    game_list = set(word_list)
    #TODO check if len(game_list) = 0 and regen if too short
    # print(game_list)
    # print(len(game_list))

# Generate a puzzle of a certain length
game_list = set()
while len(game_list) < 2:
    game_list = GeneratePuzzle.game_list

correct_list = set()
guess_list = set()


#run while there are words that haven't been found
while len(game_list) > 0:
    guess = input("guess a word: ")
    if guess in guess_list:
        print (guess + " has already been guessed")
    else:
        guess_list.add(guess)
        if guess in game_list:
            print (guess + " is a word!")
            game_list.remove(guess)
        else:
            #TODO point out what is wrong:
            # not in Dictionary
            # must have at least 4 Letters
            # must contain $center_letter
            # $letter is not in list
            print (guess + " is not a correct answer")
print ("game over, you won!")
#TODO Check validity of puzzle
#TODO Check for at least on pangram
