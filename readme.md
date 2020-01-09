# hexgram
hexgram is a project that I am creating in order to derust my programming skills for a technical interview

## Meta-Goals
I want to practice/derust the following:
* Python
* Github
* Cloud Services (especially blob storage)
* Docker

If possible I want to learn a bit about these things:
* Chat Bots
* AWS, especially S3

I'm trying to use the design standards set forth in PEP8
https://www.python.org/dev/peps/pep-0008/

## Project Goal
Create a twitch plays word find game called HEXGRAM (https://www.nytimes.com/puzzles/spelling-bee)

How to Play
Create words using letters from the hexes.
Words must contain at least 4 letters.
Words must include the center letter.
Our word list does not include words that are obscure, hyphenated, or proper nouns.

~~No cussing either, sorry.~~
Letters can be used more than once.
Score points to increase your rating.
4-letter words are worth 1 point each.
Longer words earn 1 point per letter.
Each puzzle includes at least one word which uses every letter. These are worth 7 extra points!

## To-Do
Generate letters
Choose dicionary (SOWPODS or Scrabble?)
-- remove obscure words, hyphenated word, words <4 characters, proper nouns
Generate list of words for game from Dictionary (regex)
make sure there is at least 1 fullanagram(hexgram) (word that uses every letter)
Add interactivity via chat bot (IRC?)
Create stream/display

## Dictionaries
Dictionaries were created using certain lists and cat|grep
grep command:

cat dictionaries/unprocessed/$dictname | egrep .\{4,\} > /dictionaries/$dictname

Lists found here:
Google 10k words (8906 post-processing)
https://github.com/first20hours/google-10000-english
https://github.com/zeisler/scrabble/blob/master/db/dictionary.csv

## Things to track
Whether a word has been guessed
Whether a word has been found
list of valid words

## Bonus Features
Custom dictionaries?
* Common passwords
* Pokemon/video game stuff?
* urban dictionary words of the day
* SOWPODS
* Common words

## Special Thanks
drex23
LukusAurelius
Gscookie
badacktor
ArcticRevrus
landogz
