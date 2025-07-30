master_pwd = input("What is your master password? ")

def view():
    pass

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt" ,'a') as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you want to add a new password or view existing ones? (view/add) , press 'q' to quit ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue


