# Task Add
# Task Delete
# Show Tasks
# Task as completed or not
# Exit to the app

from datetime import datetime
print("\n---Welcome to the To Do App---\n")
try:

    user_name = input("Enter your name please:  ")
    with open("Task.txt", 'w') as file:
        file.write(f"User Name: {user_name}")

except ValueError:
    print("Please Enter your name using alphabets.")

features = ("A - Add Task", "S - Show Task", "D - Delete Task", "M - Mark to Completed", "E - Exit")
print(f"Hello {user_name}\n\t\t-----This is the our features-----\n{features}")

while True:
    try:
        ask = input("\nWhat do you want to do?(A/S/D/M/E): ").lower()
        
        if ask == "a":
            print("\n------Adding New Tasks-----\n")
            add_task = input("Write your task here: ").capitalize()
            
            with open("Task.txt", "a") as file:
                file.write(f"\nTask : {add_task} |Pending || Task Adding Date & Time :  {datetime.now()} ")
            print("\n---\n Your Task Successfully Added!\n Thanks for the using our To Do App.\n---")
        
        elif ask == "s":
            print("\n-----Showing Tasks-----\n") 
            file =  open("Task.txt", "r") 
            show_task = file.read()
            print(show_task)
            file.close()

        elif ask == "m":
            print("\n-----Marking Tasks-----\n") 
            with open("Task.txt", "r") as file:
                tasks = file.readlines()
            
            updated_tasks = []


            for task in tasks:
                task = task.strip()
                status = input(f"Did you complete the task: '{task}'? (yes/no): ").strip().lower()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated_tasks.append(f"{task} - {'✅ Completed' if status == 'yes' else '❌ Not Completed'} at {timestamp}\n")


            with open("updated_tasks.txt", "w") as file:
                file.writelines(updated_tasks)

            print("Tasks updated and saved to 'updated_tasks.txt'.")

        elif ask == "d":
            del_task = input("Enter the exact task you want to delete: ").capitalize()
            with open("Task.txt", "r") as file:
                tasks = file.readlines()
            
            with open("Task.txt", "w") as file:
                for task in tasks:
                    if del_task not in task:
                        file.write(task)
            print(f"'{del_task}' deleted successfully!")


            with open("Task.txt", "r") as file:   
                file.readlines()

        elif ask == "e":
            print('GoodBye!')
            break 
    except ValueError:
        print("Please choose a valid option!")
