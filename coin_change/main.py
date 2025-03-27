"""
OVERVIEW:
Create a program that allows users to solve the Coin Change Problem by inputting a target amount and the available coin denominations. The program should load the coin denominations from a file based on the user's input of a country and then calculate the minimum number of coins needed to make the target amount. The program should also display the names of the coins used in the solution.

REQUIREMENTS:
Coin Denomination File:

Create a text or CSV file that contains the coin denominations for different countries (minimum of 4).
Comma-separated list of coin names and values (e.g., "Penny-1,Nickel-5,Dime-10,Quarter-25").
Coin Change Problem:

Implement the logic to solve the Coin Change Problem using the provided coin denominations.
The program should handle various edge cases, such as negative or zero target amounts, and invalid coin denominations.
User Interaction:

Prompt the user to enter the country for which they want to solve the Coin Change Problem.
Prompt the user to enter the target amount.
Display the minimum number of coins needed to make the target amount, as well as the names of the coins used.
Program Structure:

Use inner functions to implement the main features (loading coin denominations, solving the Coin Change Problem).
Implement helper functions for repetitive tasks (e.g., reading and parsing the coin denomination file).
Create a main function to handle user interaction and call the appropriate functions.
Error Handling:

Ensure the program handles potential errors, such as the coin denomination file not being found or the user providing invalid inputs.
SUBMISSION:
Submit a link to your completed project on GitHub in properly structured folders.
"""

#coding ts all in main you gotta change it yourself 
country_name= "America" #default preset for problem
filename= ""
currency = []



def calculate_currency(): #aacutal logic for converting said informaiton #recursion should be used here
    pass



def load_currency(country_name): #don't forget to make and get pathwat for currency_csv 
    print(country_name)
    #with open (filename, "r" ) as file:
     #   pass
    if country_name == "america": #using this to find out what information should be loaded to dictionary
        pass
    #find way to load in information to dictionrary to then be used 


def edge_handler(): #function to handle negative or 0 inputs
    pass

    

#defining menu for myself(i'm the goat)
def main():
    while True:
        print("Coin Change Problem Menu")
        print("1-Select Country Currency")
        print("2--Enter Change")
        print("3--Exit")
        calc_choice=int(input("Select what you want to use (1-3) "))
        if calc_choice== 1:
            country_name= "America"
            print('Please select what country to use')
            print(f'Currently set as {country_name} ')
            print("1-- American Dollar")
            print("2-- Antiguan Dollar")
            print("3-- Indian Rupee")
            print("4-- German Euro")
            coun_choice= int(input("What country do you want to change to(1-4): "))
            
            if coun_choice == 1: 
                country_name ="America"

            elif coun_choice == 2:
                country_name ="Antigua"

            elif coun_choice == 3:
                country_name ="India"

            elif coun_choice == 4:
                country_name ="Germany"
            else:
                print("Please select an option from (1-3)")

            load_currency(country_name)
            
        elif calc_choice== 2:
            calculate_currency(country_name)
        
        elif calc_choice== 3:
            break

if __name__ == "__main__":
  main()
