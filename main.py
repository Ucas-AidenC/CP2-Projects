#Stores all items in a list
#Function to add a new item
#Function to search the items
#Function to remove an item
#Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
#Project must include
#easy to understand variable and function names
#Pseudocode comments explaining what the code is doing
#Good use of white space to keep items separate and easy to read/find
#Have at least 2 people test your code before submission!

#List for books(editable)
library_books=[]

#book adding function
def add_book():
  title=input("What is the title of the book you want to add? ")
  









#have user select what they want to use
def main():
  while true:
    print("Personal Library Program")
    print("1- Would you like to add an item")
    print("2- Would you like to remove an item")
    print("3- Would you like to search for an item")
    print("4- Would you like to add an item")
    print("5- Display current library")
    print("6- Exit")
    choice=int(input("What would you like to use"))
        if choice== 1:
            add_book()
            
            
        elif choice== 2:
            compound_eq()
        
        elif choice== 3:
            budget()
        
        elif choice== 4:
            sale_price()
        
        elif choice== 5:
            tip_calc()
          
        elif cchoice== 6:
          break 



