# Import random module to generate computer's choice
import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get user's choice and convert to lowercase
user = input("Enter rock, paper, or scissors: ").lower()

# Computer randomly selects a choice
computer = random.choice(choices)

# Display choices
print("You chose:", user)
print("Computer chose:", computer)

# Check if user entered a valid choice
if user not in choices:
    print("Invalid choice!")

# Check for tie
elif user == computer:
    print("It's a tie!")

# Check if user wins
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")

# Otherwise computer wins
else:
    print("Computer wins!")
