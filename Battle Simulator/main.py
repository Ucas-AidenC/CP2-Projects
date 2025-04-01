#Aiden Challenger Battle simulator 
from char_handling import *
from battle_handling import *

# Selector function 
def main():
    while True:
        print("Battle Simulator")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Battle")
        print("4. See Character Stats")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            create_char()
        elif choice == "2":
            display_char()
        elif choice == "3":
            characters = load_char()
            if len(characters) < 2:
                print("Not enough characters to battle")
                continue
            
            name1 = input("What is the first character's name: ")
            name2 = input("What is the second character's name: ")
            
            char1 = next((c for c in characters if c['name'] == name1), None)
            char2 = next((c for c in characters if c['name'] == name2), None)
            
            if char1 and char2:
                battle(char1, char2)
            else:
                print("Characters not found")

        elif choice == "4":
            name = input("Enter character name to see stats: ")
            visualize_char(name)

        elif choice == "5":
            break
        else:
            print("Error try a number from 1-5")

if __name__ == "__main__":
    main()
