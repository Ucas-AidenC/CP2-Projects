#Aiden Challenger Financial Calculator
#"Create a program that completes the following basic financial calculations:

#How long it will take to save for a goal based on a weekly or monthly deposit
#Compound Interest Calculator 
#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
#Sale Price Calculator (apply discounts to prices)
#Tip Calculator


        
#goal and time calc 
def goal_calc():
#inputs
      goal= float(input("How much do you want to save? " ))
      deposit= float(input("how much can you deposit weekly? "))
#calcs 
      time = goal/deposit 
#results
      print(f"It will take {round(time, 2)} weeks to reach your goal ")

#compund equation
def compound_eq():
#inputs 
        principal = float(input("What is the starting amount "))
        rate = float(input("What is the annual interest rate (in %) ")) / 100
        time = int(input("How many times does the intrest compound "))
        years = int(input("Enter the number of years "))
#calcs 
        amount = principal * (1 + rate / time) ** (time * years)
        interest = amount - principal
#results
        print(f"Total Amount: ${round(amount, 2)}")



# budget allocation(make function, ask for percentage wanted everytime)
def budget():
#user inputs 
    income = float(input("Enter your total income: $"))
    savings_p = float(input("How much do you save annually (enter as percentage)? "))
    entertainment_p = float(input("How much do you spend on entertainment (enter as percentage)? "))
    food_p = float(input("How much do you spend on food (enter as percentage)? "))
#percent check
    if savings_p + entertainment_p + food_p > 100:
        print("Your percentages exceed 100%. Please try again.\n")
        return budget()  # Restart only if invalid input
#calc
    savings = income * (savings_p / 100)
    entertainment = income * (entertainment_p / 100)
    food = income * (food_p / 100)
    other = income - (savings + entertainment + food)
#results
    print(f"\nBudget Breakdown:")
    print(f"Savings: ${round(savings, 2)}")
    print(f"Entertainment: ${round(entertainment, 2)}")
    print(f"Food: ${round(food, 2)}")
    print(f"Other: ${round(other, 2)}")
    
    
#sale price calc (apply discount to items make function) 
def sale_price():
#inputs
  cost=float(input("how much did you pay for the item? "))
  discount= float(input("How much was the discount(enter as percentage) "))
#total calcs 
  discount_amount = cost*(discount / 100)
  end_price= cost-discount_amount
#results
  print(f"the sale price is ${round(end_price,2)}")


# tip calc (add tip to prices) (similar to discount)
def tip_calc():
#Inputs
  price=float(input("how much did you pay for the item? "))
  tip= float(input("How much was the tip (enter as percentage) "))
 #calcs
  tip_amount = price*(tip /100)
  end_cost= price+tip_amount
 #results 
  print(f"the price with tip is ${round(end_cost,2)}")
  

def main_6():
    while True:
        print("What do you wish to use? ")
        print("1-Weekly save time calculator")
        print("2-Compound intrest calculator")
        print("3-Budget allocation")
        print("4-Sale price calculator")
        print("5-Tip calculator")
        print("6-leave")
        calc_choice=int(input("Select what you want to use (1-6) "))
        if calc_choice== 1:
            goal_calc()
            
            
        elif calc_choice== 2:
            compound_eq()
        
        elif calc_choice== 3:
            budget()
        
        elif calc_choice== 4:
            sale_price()
        
        elif calc_choice== 5:
            tip_calc()
          
        elif calc_choice== 6:
          break 
if __name__ == "__main__":
  main_6()
