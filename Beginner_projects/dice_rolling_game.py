import random

while True:
    user_choice = input('Roll the dice? (y/n): ').lower()
    if user_choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            print("Congratulations, you have rolled pairs!")
        print(f"Rolled: {dice1}, {dice2} ")
    elif user_choice == 'n':
        print("Nice game!")
    else:
        raise ValueError("Invalid input")

