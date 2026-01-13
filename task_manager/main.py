# main.py

from task import Task
from storage import load_tasks, save_tasks
from validator import validate_name, validate_priority


def show_menu():
    print("\n==============================")
    print("  Task Manager Application")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    print("\n--- Add New Task ---")
    name = input("Task name: ")

    if not validate_name(name):
        print("❌ Invalid task name.")
        return

    description = input("Task description: ")
    priority = input("Priority (High/Medium/Low): ")

    if not validate_priority(priority):
        print("❌ Invalid priority.")
        return

    tasks.append(Task(name, description, priority.capitalize()))
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    print("\n--- Your Current Tasks ---")
    if not tasks:
        print("📭 No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.name} | {task.description} | Priority: {task.priority}")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to update: ")) - 1
        task = tasks[index]

        new_name = input("New name (leave blank to keep same): ")
        new_desc = input("New description (leave blank to keep same): ")
        new_priority = input("New priority (High/Medium/Low or blank): ")

        if new_name:
            if validate_name(new_name):
                task.name = new_name
            else:
                print("❌ Invalid name.")
                return

        if new_desc:
            task.description = new_desc

        if new_priority:
            if validate_priority(new_priority):
                task.priority = new_priority.capitalize()
            else:
                print("❌ Invalid priority.")
                return

        save_tasks(tasks)
        print("✅ Task updated successfully!")

    except (ValueError, IndexError):
        print("❌ Invalid selection.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1
        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            tasks.pop(index)
            save_tasks(tasks)
            print("🗑️ Task deleted successfully!")

    except (ValueError, IndexError):
        print("❌ Invalid selection.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
