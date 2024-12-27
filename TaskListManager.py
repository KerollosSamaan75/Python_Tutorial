import os

def add_task(task_list, task):
    task_list.append(task)

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)

def view_tasks(task_list):
    if task_list:
        for task in task_list:
            print(f"- {task}")
    else:
        print("No tasks available.")

def save_tasks_to_file(task_list, file_name):
    try:
        with open(file_name, 'w') as file:
            for task in task_list:
                file.write(f"{task}\n")
    except Exception as e:
        print(f"Error while saving tasks: {e}")

def load_tasks_from_file(file_name):
    task_list = []
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                task_list = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error while loading tasks: {e}")
    return task_list

def main():
    file_name = "tasks.txt"
    tasks = load_tasks_from_file(file_name)

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks_to_file(tasks, file_name)
            break
        else:
            print("Invalid option. Please try again.")

main()
