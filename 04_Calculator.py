# Power (num1 ** num2)
# Square root (math.sqrt(num))
# Modulo (%)
# Floor division (//)
# Factorial, sin, cos, log (math library)
import math
print("A - Add")   
print("S - Substract")   
print("D - Divide")   
print("M - Multiply")  
print("P - Power") 
print("E - Exit\n")

while True:
    ask_user = input("What do you want do?(A/S/D/M/E): ").lower().strip()
    try:

        if ask_user == "e":
            print("GoodBye!")
            quit()
        if ask_user == "a":
            print("\n----- Adding Process -----\n")
            first = float(input("Enter The First Number: "))
            second = float(input("Enter The Second Number: "))
            add = first + second
            print(f"The sum of number is {add}")

        elif ask_user == "s":
            print("\n----- Substract Process -----\n")
            first = float(input("Enter The First Number: "))
            second = float(input("Enter The Second Number: "))
            subs = first - second
            print(f"The substract of the number {subs}")
        
        elif ask_user == "m":
            print("\n----- Multiply Process -----\n")
            first = float(input("Enter The First Number: "))
            second = float(input("Enter The Second Number: "))
            mul = first* second
            print(f"The multiplication of number is {mul}")    
        
        elif ask_user == "d":
            print("\n----- Divide Process -----\n")
            first = float(input("Enter The First Number: "))
            second = float(input("Enter The Second Number: "))
            div = first/second
            print(f"The division of you numbers is {div}")
        
        elif ask_user == "p":
            print("\n----- Get Power Process -----\n")
            first = float(input("Which num do you want a square: "))
            sq = first*first
            print(f"The sqaure of the number is {sq}")
            
    except ValueError:
        print("Please enter a valid number.")