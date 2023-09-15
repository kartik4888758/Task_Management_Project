import os
import json


TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if tasks:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{index}. Title: {task['title']}, Description: {task['description']}, Status: {status}")
    else:
        print("\nNo tasks to display.")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print(f"Task '{tasks[choice - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number. No task marked as completed.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            deleted_task = tasks.pop(choice - 1)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number. No task deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
