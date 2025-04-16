#Aiden Challenger Password Generator

#Functions for the different password requirements
#A function that assembles that password once it is the correct length
#Users should be able to specify length and if they want to include
#uppercase letters
#lowercase letters
#numbers
#special characters

import random

# List defining  
password_history_list = []

uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "<", ">", ",", ".", "/", "?"]

# Password generator  
def password_gen(length, uppercase, lowercase, number, special):
    password = []
    
    if uppercase == "yes":
        password += uppercase_letters
    if lowercase == "yes":
        password += lowercase_letters
    if number == "yes":
        password += numbers
    if special == "yes":
        password += special_characters

    if not password:  # check if all are set to "no"
        print("at least one must be selected")
        return
#printing results 
    print("\nGenerated Passwords:")
    for i in range(4):
        password_p = "".join(random.choices(password, k=length))
        print(password_p)
        password_history_list.append(password_p)


# take parameters
def parameters_g():
    while True:
        try:
            length = int(input("How long do you want the password? "))  
            if length <= 0:
                print(" must be higher than zero")
                continue  # try again
            break  
        except ValueError:
            print("Error: Please enter a valid number.")

    def get_yes_no(prompt):
        response = input(prompt).strip().lower() or "yes"  # default to "yes"
        if response not in ["yes", "no"]:
            print("Please only use yes or no ")
            return None  
        return response  

    while True:
        uppercase = get_yes_no("Do you want uppercase letters (yes/no)? ")
        lowercase = get_yes_no("Do you want lowercase letters (yes/no)? ")
        number = get_yes_no("Do you want numbers (yes/no)? ")
        special = get_yes_no("Do you want special characters (yes/no)? ")

        if None in [uppercase, lowercase, number, special]:  # If any invalid response, ask again  
            continue  

        if uppercase == "no" and lowercase == "no" and number == "no" and special == "no":
            print("at least one option must be yes")
            continue  # try again
        
        return length, uppercase, lowercase, number, special  #return the values

# history function  
def password_history():
    print("\nPassword History:")
    for i, password in enumerate(password_history_list, 1):
        print(f"{i}: {password}")

# main/menu function  
def main_3():
    length, uppercase, lowercase, number, special = parameters_g()  # Initialize parameters  

    while True:
        print("\nWhat do you want to use")  
        print("1. Password Generator")
        print("2. Password History")  
        print("3. Set Parameters")
        print("4. Quit")
        choice = input("Please select what you want to use: ")

        if choice == "1":
            password_gen(length, uppercase, lowercase, number, special)
        elif choice == "2":
            password_history()
        elif choice == "3":
            length, uppercase, lowercase, number, special = parameters_g()  # Update parameters  
        elif choice == "4":
            break
        else:
            print("Please select a number from 1-4 ")

if __name__ == "__main__":
    main_3()
