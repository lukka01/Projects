def todo_list_manager():
    tasks = []

    print("Welcome to your To-Do List Manager!")
    print("Commands: 'add', 'view', 'remove', 'exit'")

    while True:
        command = input("What would you like to do? ").lower()

        if command == 'add':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"Task '{task}' added to your list!")

        elif command == 'view':
            if not tasks:
                print("Your to-do list is empty!")
            else:
                print("\nYour To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif command == 'remove':
            if not tasks:
                print("Your to-do list is already empty!")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start = 1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("Enter the number of the task to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' removed!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number! ")

        elif command == 'exit':
            print("Goodbye! Your tasks have been saved")
            break

        else:
            print("Invalid command! Please use: 'add', 'view', 'remove', or 'exit'")



todo_list_manager()