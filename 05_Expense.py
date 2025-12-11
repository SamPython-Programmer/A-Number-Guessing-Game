# Welcome to Expense Tracker!
# 1. Add Expense
# 2. View Expenses
# 3. Delete Expense
# 5. Exit

from datetime import date
print("---- Welcome to Expense Tracker! ----")
user_name = input("Enter your name please: ")
print(f"___\tHello! {user_name}______\n______Options______  ")

features = {
            'A' : "Add Expenses",
            'V' : "View Expenses",
            'D' : "Delete Expenses",
            'E' : "Exit to the Expenses tracker"
        }

for key, value in features.items():
    print(f"{key} - {value}")
        
while True:        
    try:
        ask_user = input("Which one you like to do: ").lower().strip()
        
        if ask_user == "e":
            print("GoodBye!")
            quit()
        elif ask_user == "a" :
            print("----- Adding Expenses -----\n")
            expense = int(input("Enter the today's expense: "))    
            where = input("Enter the reason why you expense the money: ")
            with open("Expense.txt", "a") as file:
                file.write(f"\nMr. {user_name}\nYour {str(expense)} money is expense by {where} due to {date.today()} on {date.today().strftime("%A")} .")
                print("Your expenses successfully added!\n")
        
        elif ask_user == "v":
            print("----- Viewing Tasks -----\n")
            file = open("Expense.txt", "r")
            text = file.read()               
            print(text, end= "\n")
            file.close   
        
        elif ask_user == "d":
            print("----- Deleting Expenses -----\n")
            with open("Expense.txt", "r") as file:
                file.readlines()
                print("Are you sure to delete all your expenses?")
            confirmation = input("Type 'yes' to confirm or 'no' to cancel: ").lower().strip()
            if confirmation == "yes":   
                open("Expense.txt", "w").close()    
                print("All your expenses are deleted successfully!\n")        
            else:
                print("Operation cancelled!\n")
    except ValueError:
            print("Invalid Input!\n")