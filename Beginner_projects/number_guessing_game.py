import random


number_to_guess = random.randint(1,100)

while True:
    try:
        user_guess = int(input("Guess the number from 1 to 100: "))

        if user_guess < number_to_guess:
            print("The number is too low! ")
        elif user_guess > number_to_guess:
            print("The number is to high! ")
        else:
            print("Congratulations, you have guessed the number! ")
            break

    except ValueError:
        print('Please enter a valid number! ')
