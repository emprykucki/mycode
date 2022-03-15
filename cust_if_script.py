#!/usr/bin/env python3
"""EMP Python Training Day 2 - Custom Code Harry Potter Titles 
    if, elif, else - A simple program using conditionals to make a decision."""

# Repeated message
message = 'Harry Potter and ... '

#Opening Message: wrap connection in a float() to accept decimals as numbers
book = float(input("Which Harry Potter book are you interested in?"))

#if input value 
if book == 1:
    message = message + 'The Sorcerer\'s Stone'

elif book == 2:
    message = message + 'The Chamber of Secrets'

elif book == 3:
    message = message + 'The Prisoner of Azkaban'

elif book == 4:
    message = message + 'The Goblet of Fire'

elif book == 5:
    message = message + 'The Order of the Phoenix'

elif book == 6:
    message = message + 'The Half Blood Prince'

elif book == 7:
    message = message + 'The Deathly Hallows'

elif book > 7:
    message = message + 'Maybe Someday'
    
else:
    message = message + 'You\'re Funny'

print(message)

print('Mischief Managed')


