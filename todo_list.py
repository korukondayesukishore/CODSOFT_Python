print("To-Do List Application")
print("Created by Ramana")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("Your Tasks:")
            for t in tasks:
                print("-", t)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid option")
