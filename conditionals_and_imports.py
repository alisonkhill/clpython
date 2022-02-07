# Comparators in Python
    # < less than
    # <= less than or equal to
    # == equal
    # >= greater than or equal to
    # > greater than
    # != not equal
# Assignment is one = while equality is two ==

# if statements
    # else if = elif in python
    # syntax: if variable > integer:
    # can also use or: if variable > integer1 or < integer2:
    # else: elif:

# look for ways to combine so you're not running the same code over and over

# not operator negates a comparison, for example:

"""
forecast = "rain"

if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")
"""
# else statement is run

# Another way to do the same thing:

"""
raining = True

if raining:
    print("Stay inside!")
else:
    print("Go Outside!")
"""

# Boolean values must be capitalized

# Python standard library tells you what's built in. Here we'll use the random module in the Math section

import random

computer_throw = random.choice(["rock", "paper", "scissors"])

my_throw = input("Let's play Rock, Paper, Scissors. Enter your choice\n")

if computer_throw == my_throw:
    print("We tied.")
elif my_throw == "rock" and computer_throw == "scissors":
    print("you threw " + my_throw + ". You win.")
elif my_throw == "paper" and computer_throw == "rock":
    print("you threw " + my_throw + ". You win.")
elif my_throw == "scissors" and computer_throw == "paper":
    print("you threw" + my_throw + ". You win.")
else:
    print("I win.")

print("I threw " + computer_throw)