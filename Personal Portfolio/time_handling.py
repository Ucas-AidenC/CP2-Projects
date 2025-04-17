#file for reading time 

import time

def get_timestamp():
    #returingg ffille info as a strning 
    return time.strftime("%Y-%m-%d %H:%M:%S")

def take_time(filepath):
    # #read file and return the conntent 
    with open(filepath, "r") as file:
        content = file.read()
    
    timestamp = get_timestamp()
    
    return content, timestamp

if __name__ == "__main__":
    get_timestamp()
