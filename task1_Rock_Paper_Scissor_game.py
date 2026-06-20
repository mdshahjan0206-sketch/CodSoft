import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = input("Enter your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    elif user in choices:
        print("Computer Wins!")
        computer_score += 1

    else:
        print("Invalid Choice!")
        continue

    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Thanks for playing!")
