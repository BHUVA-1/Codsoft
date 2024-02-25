import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} - {'Done' if task['completed'] else 'Pending'}")

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks, index, completed):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = completed
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter the task index to update: "))
            completed = input("Mark as completed? (y/n): ").lower() == 'y'
            update_task(tasks, index, completed)
        elif choice == "4":
            show_tasks(tasks)
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

