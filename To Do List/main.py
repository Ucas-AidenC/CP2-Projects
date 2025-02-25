tasks = {
}
#vasriables that should be updated and send update to 
with open(To Do List/.txt, "r") as file:
    for line in file:
    parts = line.strip().split(" | ")
    if len(parts) == 2:
    task, status = parts
    tasks[task] = status
print(tasks)

def load_tasks():
    """Loads tasks from the to-do list file into a dictionary."""
    tasks = {}
    try:
        with open(TODO_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    task, status = parts
                    tasks[task] = status
        # If file doesn't exist, return an empty task list
        tasks = {}

    return tasks

with open ("To Do List/To Do List.txt", "r") as file: 
    data = To Do List.txt 
    #should save as a editable variable (dictiornat  9 )
    #variable name here.uppdate = data 
    


#def add():
#    with open ("To Do List/.csv", "r") as file: 
 #       add_v = input("wha would you like to add to you to do list? ").strip()
 #       file.write (“add_v”)

def remove(): 




def mark_done(): 


