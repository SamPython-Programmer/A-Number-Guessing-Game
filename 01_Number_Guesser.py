import random

random_number = random.randint(0, 100)
attempts = 0
play = input("Do you want to play?(yes/no) ").lower()
try:
    if play != "yes":
        print("Goodbye!")
        quit()
    else:
        print("_____ Let's play:) _____")

except ValueError:
    print("Please enter a valid number.")

while True:
    try:
        user_guess = input("Guess the number between (1- 100): ")
    except ValueError:
        print("Please enter a valid number.")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        attempts += 1
        
        if user_guess > random_number:
            print("Lower number please!")
        
        elif user_guess < random_number:
            print("Higher number please!")
        elif user_guess == random_number:
            print(f"Crongatulations! You guessed the number in {attempts} attempts.") 
            quit("Thanks for play.")