#Aiden Challenger Coin Change 
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



from cur_handling import *

#main selector function 
def main():
    country_name = "America"  # Default
    currency = load_currency(country_name)

    while True:
        print("\nCoin Change Problem Menu")
        print("1 - Select Country Currency")
        print("2 - Enter Change Amount")
        print("3 - Exit")
        
        choice = int(input("Select an option (1-3): "))

        if choice == 1:
            print("1 - American Dollar\n2 - Antiguan Dollar\n3 - Indian Rupee\n4 - German Euro")
            coun_choice = input("Enter choice (1-4): ").strip()

            country_map = {"1": "America", "2": "Antigua", "3": "India", "4": "Germany"}
            country_name = country_map.get(coun_choice, country_name)
            currency = load_currency(country_name)

        elif choice == 2:
            try:
                amount = int(input("Enter target amount: ").strip())
                calculate_currency(amount, currency)
            except ValueError:
                print("Error enter a interger")

        elif choice == 3:
            break

        else:
            print("Error select a number 1-3")

if __name__ == "__main__":
    main()
