to_do_list = []
completed_task = []
def show_menu():
    print("To-Do List Manager")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as completed")
    print("4. View Completed Tasks")
    print("5. Replace Task")
    print("6. Exit")

def add_task(): 
    task = input("Enter the task you want to add: ")
    to_do_list.append(task)
    print(f"Task {task} added to the list!")

def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty!")
    else: 
        print("Your To-Do List: ")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
    
def complete_task():
    if not to_do_list:
        print("Your to-do list is empty! No tasks to complete.")
    else: 
        view_tasks()
        try: 
            task_num = int(input("Enter the number of the task you completed: "))
            task = to_do_list.pop(task_num - 1)
            completed_task.append(task)
            print(f"'{completed_task}' ,marked as completed!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

def view_completed_tasks():
    if not completed_task:
        print("No tasks completed yet!")
    else:
        print("Completed Tasks: ")
        for i, task in enumerate(completed_task, 1):
            print(f"{i}. {task}")

def replace_task():
    if not to_do_list:
        print("Your to-do list is empty! No tasks to replace.")
    else: 
        view_tasks()
    try:
        rep_task = int(input("Which task do you want to replace?: "))
        if 1 <= rep_task <= len(to_do_list):
            new_task = input("Enter the new task: ")
            old_task = to_do_list[rep_task - 1]
            to_do_list[rep_task - 1] = new_task
        else:
            print(f"{old_task} is replaced with {new_task}")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

    
    





while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        view_completed_tasks()
    elif choice == "5":
        replace_task()
    elif choice == "6":
        print("Goodbye! Have a productive day!")
        break
    else: 
        print("Invalid choice. Please choose a valid option (1-5).")
