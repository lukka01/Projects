import random

from Tools.scripts.mailerdaemon import emparse_list_list

Rock = 'r'
Paper = 'p'
Scissors = 's'

emojis = { Rock: '✊', Paper: '✋', Scissors: '✌️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        users_choice = input("Rock, paper or scissors? (r/p/s): ")
        if users_choice in choices:
           return users_choice
        else:
            print("Invalid input! ")

def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == Rock and computer_choice == Scissors) or
        (user_choice == Scissors and computer_choice == Paper) or
        (user_choice == Paper and computer_choice == Rock)):
        print('You won! ')
    else:
        print("You lost! ")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == 'n':
            break

play_game()







