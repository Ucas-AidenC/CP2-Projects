from file_handling import *
from time_handling import*

def main_5(): 
    while True: 
        print("\nMain Menu")
        print("1. Read file")
        print("2. Write to file")
        print("3. Exit")
        
        choice = int(input("What do you want to do?: \n"))
            
        if choice == 1:
            filepath = input("Enter the file path to read: \n")#user inpuut for file 
                
            content, timestamp = take_time(filepath)  #reading file and giving it timestamp 
            print("\nFile Content:\n", content)
            print(f"\nLast Updated: {timestamp}")

        elif choice == 2:
            filepath = input("Enter the file path to write to: \n")#file paath and text enterign 
            new_text = input("Enter text to add: \n")
                
            write_file(filepath, new_text)   #function callingg from other file 

        elif choice == 3:
            break


if __name__ == "__main__":
    main_5()
