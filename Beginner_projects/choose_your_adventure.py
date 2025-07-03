name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input("You are on a dirt road, choose the path between left and right: ").lower()
if answer == "left":
    answer = input("You came across the river, you can walk around it or swim (swim/walk) ").lower()
    if answer == 'swim':
        print("You have been eaten by the crocodile, game over")
    elif answer == 'walk':
        print("You have survived")
    else:
        print("Invalid option")
elif answer == "right":
    answer = input("You have to cross the bridge, it's wobbly, do you want to cross it or not?(cross/back) ").lower()
    if answer == "cross":
        print("The Bridge has fallen , game over.")
    elif answer == "back":
        answer = input("Now you must take the weapon (knife/Bow) ").lower()
        if answer == "bow":
            print("You lost!")
        elif answer == "knife":
            print("You won!")
    else:
        print("Invalid option")
else:
    print("Invalid option! ")


