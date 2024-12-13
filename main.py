# Import library of functions
import file_control

def main():
    '''
    Main function to execute the Task Tracker program.
    '''
    # Get tasks from file
    tasks = file_control.load_tasks()

    # Create loop for menu
    while True:
        print("---Task Tracker Menu---")
        print("1. Display tasks",
              "\n2. Add tasks",
              "\n3. Mark task as complete",
              "\n4. Save and exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Navigate user based on choice
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
        elif choice == "3":
            tasks = complete(tasks)
        elif choice == "4":
            file_control.save_tasks(tasks)
            print("Thank you for using Task Tracker.")
            break
        else:
            print("That is not a valid option. Please try again.")

def display_tasks(tasks):
    '''
    Function to display all tasks in the list with their details.
    :param tasks: list of tasks
    :return: None
    '''
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks):
            print(f"\nTask {index + 1}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Status: {'Complete' if task['status'] else 'Not Complete'}")

def add_task(tasks):
    '''
    Function to add a new task to the list.
    :param tasks: list of tasks
    :return: updated list of tasks
    '''
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    due_date = input("Enter the due date (e.g., MM/DD/YYYY): ")
    status = False  # Default to not complete
    tasks.append({"title": title, "description": description, "due_date": due_date, "status": status})
    print("Task added successfully!")
    return tasks

def complete(tasks):
    '''
    Function to mark a task as complete.
    :param tasks: list of tasks
    :return: updated list of tasks
    '''
    if not tasks:
        print("No tasks to mark as complete.")
    else:
        display_tasks(tasks)
        try:
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["status"] = True
                print(f"Task {task_number + 1} marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    return tasks

# Conditionally execute the main function
if __name__ == "__main__":
    main()
