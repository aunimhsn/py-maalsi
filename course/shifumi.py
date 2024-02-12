
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

while user_score != 2 and computer_score != 2:

    # User's choice / Computer's choice
    print("Please choose between: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = choices[int(input("")) - 1]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice: # Draw
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "Rock": # Case: User choose "Rock"
        if computer_choice == "Paper":
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1
    elif user_choice == "Paper": # Case: User choose "Paper"
        if computer_choice == "Scissors":
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1
    elif user_choice == "Scissors": # Case: User choose "Scissors"
        if computer_choice == "Rock":
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1   

print(f"Computer: {computer_score} - User: {user_score}")