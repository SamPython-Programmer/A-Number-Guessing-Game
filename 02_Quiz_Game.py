print("------Welcome to the Quiz Game!-------\n")

playing = input("Do you want to play?(yes/no) ").lower()

if playing != "yes":
    print("Goodbye!")
    quit()

print("Okay! Let's play:) ")

score = 0

answer = input("What is the full form of C.P.U.? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of G.P.U.? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of RAM? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of ROM? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {str(score)} quetions correct!")
print(f"You got {str(score)/4*100}%.")