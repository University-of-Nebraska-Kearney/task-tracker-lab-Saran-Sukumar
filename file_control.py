import json

def load_tasks():
    '''
    Function to load tasks from a file into a list.
    Reads tasks from "tasks.json" and returns them as a list.
    If the file does not exist, returns an empty list.
    '''
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)  # Read and return the list of tasks
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error: The tasks file is corrupted. Starting with an empty list.")
        return []  # Return an empty list if the file's content is invalid JSON

def save_tasks(tasks):
    '''
    Function to save a list of tasks to a file for long-term storage.
    Writes tasks to "tasks.json".
    '''
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)  # Save the list of tasks in JSON format
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error: Could not save tasks. {e}")
