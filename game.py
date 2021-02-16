# game.py

import random

#import os
#from dotenv import load_dotenv

#load_dotenv()
#player_name = input("Hi! Please enter your name:")

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking user for an input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
print("-------------------")

print("You chose:", user_choice)

#
#validate the user selection
#

options = ["rock", "paper", "scissors"]
user_choice.lower()

if user_choice in options:
    pass
else:
    print("Oops. Please choose a valid option and try again.")
    exit()

#
#simulating a computer input
#

computer_choice = random.choice(options)

print("The computer chose:", computer_choice)

#
#determining who won
#

print("-------------------")
if user_choice == "rock":
    if computer_choice == "rock":
        print("Oh, it's a tie.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Oh, it's a tie.")
else:
    print("OOPS SOMETHING WENT WRONG.")

print("-------------------")
print("Thanks for playing. Please play again!")