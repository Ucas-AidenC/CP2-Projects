
#folder for the actual calcs and such 
import csv

#function for loading the currency of a country 
def load_currency(country_name):
    currency = []

    with open("Coin Change/currencies.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == country_name:  #matching the country 
                for entry in row[1:]:  
                    name, value = entry.split('-')#split with - instead of comma 
                    currency.append((name, int(value)))
                break 
#check for if it's real 
    if not currency:
        print(f"Error No currency found for {country_name}")
    
    return sorted(currency, key=lambda x: -x[1])  #sorting the keys by their value 

#function for calculating the amount
def calculate_currency(target_amount, currency):
    if target_amount <= 0:
        print("Error be greater than zero.")
        return

    coin_count = {}
    remaining = target_amount

    for name, value in currency:
        if remaining >= value:
            count = remaining // value
            coin_count[name] = count
            remaining -= count * value

    if remaining == 0:
        print(f"Minimum coins needed: {sum(coin_count.values())}")
        for name, count in coin_count.items():
            print(f"{name}: {count}")
    else:
        print("Not possible with current denominations")
