from zoneinfo import reset_tzpath

print("Welcome to he quiz game! ")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay, let's play game! ")
score = 0

answer = input("Where is the Central park located? ")
if answer.lower() == "new york":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Where is the world's largest city? ")
if answer.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} points! ")