#Aiden Challenger Financial Calculator
#"Create a program that completes the following basic financial calculations:

#How long it will take to save for a goal based on a weekly or monthly deposit
#Compound Interest Calculator 
#Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
#Sale Price Calculator (apply discounts to prices)
#Tip Calculator

#take goal+ deposit( seperate from and before selction )(don't forgor rounding)
def main():
    while True:
        print("What do you wish to use")
        print("1-Weekly save time calculator")
        print("2-Compound intrest calculator")
        Print("3-Budget allocation")
        Print("4-Sale price calculator")
        Print("5-Tip calculator")
        calc_choice=int(input("which one do you want to use(1-5)"))
        if calc_choice== 1:
            save_time_calc()
            
            
        elif calc_choice== 2:
            pass
        
        elif calc_choice== 3:
            pass
        
        elif calc_choice== 4:
            pass
        
        elif calc_choice== 5:
            pass
        
        

#ask user what they want to use(prob use words not numbers)(maybe have function for switching to ignore caps)(ensure it asks multiple times after last function completes) (i'm cooked)(lowk just make this the ian function)(bruh fix that ugle code) 
def save_time_calc():
      goal= float(input("How much do you want to save?"))
      deposit= float(input("how much can you deposit weekly"))
      time = goal/deposit 
      print("It will take {round(time, 2) years to reach your goal 


#compund equation




# budget allocation(make function, ask for percentage wanted everytime)(find way to get tme into ask)(side function)
def saving():
    income=
    savings=int(input("How much do you save annually "))
    entertainment=int(input("How much do you spend on entertainment"))
    food=int(input("How much do you spend on food "))
#sale price calc (apply discount to items make function) 

# tip calc (add tip to prices)

