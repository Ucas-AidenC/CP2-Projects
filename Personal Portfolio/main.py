
#Aiden Challenger, Personal Portfolio 

#importing from other existing files 
from Movie_recommender import *
from MorseCode import *
from Password_generator import *
from To_Do_list import *
from word_counter import *
from fiancal_calculator import *



#What the project does
#
#How you found the programming process
#
#What you learned
#
#Your role (if it was a group project)

#defining the actual main nthat will serve as the menu to open the other mains
def main(): 
    while True:
        print("\nPersonal Portfolio")
        print("1. Movie Recommender")
        print("2. Morse Code Translator")
        print("3. Password Generator")
        print("4. To Do List")
        print("5. Word Counter")
        print("6. Financial Calculator")
        print("7. Exit Program")


        choice = int(input("What would you like to do (1-7)? "))
       
       #Movie Code 
        if choice == 1: 
            print("This project takes parameters for diffrent movies then gives the users recomendations for movies they should watch")
            print("I found the coding process for this to be a little weird because I was initally overwhelmed by the amount of data on the list I had to sort through")
            print("Through this I learned file handling for txts and how to use multiple python files\n")
            main_1()
        

        #Morse code program 
        elif choice == 2:
            print("This project takes an input from user for a phrase in english or more then translates between the two ")
            print("The coding process for this was fun because it was kinda like solving a puzzle in a way")
            print("I learned diffrent methods of handling user inputs\n")
            main_2() 
        
        #Password gen menu 
        elif choice == 3:
            print("This project is a password generator that generates passwords based on set parameters")
            print("I learned how to handle and save varibles to be reusewd in a seperate piece of code")
            print("I found the coding process to be relativly easy with the main issue being the creation of lists\n")
            main_3()
        
        #To do list program 
        elif choice == 4:
            print("This project allows the user to create a to do list based on what they input")
            print("The coding process for this was fun because it allowed me to edit a file more then is usually done ")
            print("I learned about file editing and how to change an exiting file and modify prexisting elements\n ")
            main_4()
        
        #Word counter program 
        elif choice == 5:
            print("This project takes the filepath for a txt document then gives the amount of words along with a time stamp on when it was last checked")
            print("I found the coding process for this to be quite unique becasue it required taking information from a none preset file")
            print("Through this I learned file handling for txts and how to use multiple python files\n")
            main_5()
        
        #Financial calc code 
        elif choice == 6:
            print("This project takes inputs from user for what they want to use then runs the required ")
            print("I found the coding process for this to be a bit difficult because it was when I returned from coding after taking a year break")
            print("Through this I relearned several of the code basics I had forgotten\n")
            main_6()

        elif choice ==7:
            break

        else:
            print("Please select a number from 1-7")

#code run
if __name__ == "__main__" :
    main()
