#Aiden Challenger Password Generator

#Functions for the different password requirements
#A function that assembles that password once it is the correct length
#Users should be able to specify length and if they want to include
#uppercase letters
#lowercase letters
#numbers
#special characters


#summoning random

import random
#list defining 
password_history_list = []

uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "<", ">", ",", ".", "/", "?"]




#password gen 
def password_gen():
#asking user what they want in a password 
  length=int(input("how long do you want the password: "))
  uppercase=input("do you want uppercase letters(yes/no): ")
  lowercase=input("do you want lowercase letters(yes/no): ")
  number=input("do you want numbers(yes/no): ")
  special=input("do you want special characters(yes/no): ")
  
  #adding info to gen password
  password=[]
  if uppercase == "yes":
      password+=uppercase_letters
  if lowercase == "yes":
      password+=lowercase_letters
  if number == "yes":
      password+=numbers
  if special == "yes":
      password+=special_characters
  print("\nGenerated Passwords:")
  for i in range(4):
    password_p = "".join(random.choices(password, k=length))
    print(password_p)
    password_history_list.append(password_p)





#history 
def password_history():
    print("\nPassword History:")
    for i, password in enumerate(password_history_list, 1):
        print(f"{i}: {password}")




#main/ selector 
def main():
  while True: 
      print("What do you want to use") 
      print("1. Password Generator")
      print("2. Password History") 
      print("3. quit")
      choice=int(input("Please select what you want to use: "))

      if choice==1: 
        password_gen()

      if choice==2: 
        password_history()
        
      if choice==3: 
        break
  
  
if __name__ == "__main__":
    main()
