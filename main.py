'''
The project is about To-Do List that includes add, view and remove tasks
'''


RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

tasks = []
print("Welcome to Your To-Do List App!\n")

def display_menu():   # Function at the start of project to display menu
    #print("To-Do List\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit\n")

def add_task():   # Add Task
    print("Option 1: Add Task\n")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    tasks.append({"Title" : title, "Description" : description})
    print(f"\n{GREEN}Task Added Successfully!{RESET}\n")

def view_tasks():   # View Tasks
    print("Option 2: View Tasks\n")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. Title: {task['Title']}\n   Description: {task['Description']}\n") 

def remove_tasks():   # Remove Task
    view_tasks()
    choice = input("Enter the number of the task to remove(0 to cancel): ")
    if choice.isdigit() and int(choice) >= 0 and int(choice) <= len(tasks):
        if int(choice) == 0:
            return
        removed_tasks = tasks.pop(int(choice) - 1)
        print(f"\n{GREEN}Task '{removed_tasks['Title']}' Removed Successfully!{RESET}\n")
    else:
        print(f"{RED}\nInvalid input. Please enter a valid task number.{RESET}\n")

# Main Program
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_tasks()
    elif choice == '4':
        print("Exiting The To-Do List App. Good Bye!\n")
        break
    else:
        print(f"\n{RED}Invalid choice. Please enter a number between 1 - 4.{RESET}\n")
