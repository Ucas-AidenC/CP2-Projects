tasks = {}

#adding tasks to dictionary 
def load_tasks(file_path):
    with open("To Do List/.txt", "r") as file:
        for line in file:
            task, status = line.strip().split("|")
            tasks[task] = status == "True"
    return tasks

#save tasks to the main file 
def save_tasks():
    with open(file_path, "a") as file:
        for task, completed in tasks.items():
            file.write(f"{task}|{completed}\n")

#pritn tasks and if they're done 
def view_items():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, (task, completed) in enumerate(tasks.items(), 1):
            status = "Completed" if completed else "Not Completed"
            print(f"{idx}. {task} - {status}")

#add new task to dictionary 
def add_item():
    new_task = input("Enter the new task: ")
    if new_task in tasks:
        print("task already exists")
    else:
        tasks[new_task] = False
        save_tasks()

#remove a task function 
def remove_item():
    task_number = int(input("Enter the task number to remove: "))
#check number 
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        removed_task = task_list[task_number - 1]
        del tasks[removed_task]
#save new list to file 
        save_tasks() 

#mark task as completed
def mark_item():
    task_number = int(input("Enter the task number to mark as completed: "))
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        task = task_list[task_number - 1]
        tasks[task] = True
        print(f"Task '{task}' marked as completed")

def main():
    file_path = "To Do List/.txt"
    tasks = load_tasks("To Do List/.txt")
    while True:
        print("\nTo Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice ")

        if choice == "1":
            view_items()
        elif choice == "2":
            add_item(tasks, new_task)
        elif choice == "3":
            view_items()
            remove_item(tasks, task_number)
        elif choice == "4":
            view_items()
            mark_item(tasks, task_number)
        elif choice == "5":
            save_tasks()
            break

if __name__ == "__main__":
    main()
