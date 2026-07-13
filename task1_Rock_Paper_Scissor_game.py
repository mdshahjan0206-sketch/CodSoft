# Import random module to generate computer's choice
import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Repeat the program until the user chooses to exit
while True:

    # Display the menu
    print("\n----- Rock Paper Scissors -----")
    print("1. Play Game")
    print("2. Exit")

    # Get the user's menu choice
    choice = int(input("Enter your choice: "))

    # Check if the user wants to play
    if choice == 1:

        # Get the user's choice and convert it to lowercase
        user = input("Enter rock, paper, or scissors: ").lower()

        # Check whether the entered choice is valid
        if user not in choices:
            print("Invalid choice!")
            continue

        # Computer randomly selects a choice
        computer = random.choice(choices)

        # Display the choices
        print("You chose:", user)
        print("Computer chose:", computer)

        # Check for a tie
        if user == computer:
            print("It's a tie!")

        # Check if the user wins
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")

        # Otherwise, the computer wins
        else:
            print("Computer wins!")

    # Exit the program if the user chooses option 2
    elif choice == 2:
        print("Thank you for playing!")
        break

    # Display an error message for an invalid menu option
    else:
        print("Invalid menu choice!")
