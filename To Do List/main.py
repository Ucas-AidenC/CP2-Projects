#Aiden Challenger, To Do List

# what i will save info to
tasks = {}

#used this in place of "To Do List/To Do List.txt"
file_path = "To Do List/To Do List.txt"


# load tasks from file
def load_tasks(file_path):
    with open(file_path, "r") as file:
        for line in file:
            task, status = line.strip().split("|")
            tasks[task] = status == "True"
    return tasks

# save tasks to file
def save_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        for task, completed in tasks.items():
            file.write(f"{task}|{completed}\n")

# print list based on file
def view_tasks(tasks):
    #check if task exists yet 
    if not tasks:
        print("no task found")
    #printing tasks 
    else:
        for idx, (task, completed) in enumerate(tasks.items(), 1):
            status = "Completed" if completed else "Not Completed"
            print(f"{idx}. {task} - {status}")

# add task and save to file
def add_tasks(file_path, tasks):
    #take nnew task info 
    new_task = input("Enter the new task: ").strip()
    if new_task in tasks:
        print("Task already exists")
    else:
        tasks[new_task] = False
        #save new info 
        save_tasks(file_path, tasks)

# remove task and save to file
def remove_tasks(file_path, tasks):
    view_tasks(tasks)
    #check number that will be removed 
    task_number = int(input("Enter the task number to remove: "))
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        removed_task = task_list[task_number - 1]
        del tasks[removed_task]
        #save new info 
        save_tasks(file_path, tasks)

# make task complete
def mark_tasks(file_path, tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        task = task_list[task_number - 1]
        tasks[task] = True
        save_tasks(file_path, tasks)

# selector function 
def main():
    tasks = load_tasks(file_path)
    while True:
        print("\nTo Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. remove Task")
        print("4. make task completed")
        print("5. quit")
        choice = int(input("what do you want to use(1-5): "))
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_tasks(file_path, tasks)
        elif choice == 3:
            remove_tasks(file_path, tasks)
        elif choice == 4:
            mark_tasks(file_path, tasks)
        elif choice == 5:
            save_tasks(file_path, tasks)
            break

if __name__ == "__main__":
    main()
