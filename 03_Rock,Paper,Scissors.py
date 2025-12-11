import random

items = {1: "rock", 2: "paper", 3: "scissors"}
user_wins = 0
computer_wins = 0
attempts = 0
draw = 0
while True:
    computer_choice = random.randint(1, 3)
    computer = items[computer_choice]
    
    user = input("Choose (Rock/Paper/Scissors): ").lower().strip()
    attempts += 1
    if user not in items.values():
        print("Invalid input! Please choose Rock, Paper, or Scissors.\n")
        continue

    print(f"Computer choose: {computer}\nYou choose: {user}")       

    if user == computer:
        print("It's a draw!\n")
        draw += 1
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!\n")
        user_wins += 1
    else:
        print("You lose!\n")
        computer_wins += 1
    if attempts == 10:
        print(f"You win the game {user_wins} times and {computer_wins} times lose and {draw} times draw.")
        quit()

                    