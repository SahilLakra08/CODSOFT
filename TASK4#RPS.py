#TASK 4
# Rock-Paper-Scissors Game
import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_input = input("\nChoose rock, paper, or scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    """Display the choices and the result of the round."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_again():
    """Ask the user if they want to play another round."""
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

print("Welcome to CodSoft Rock-Paper-Scissors Game!")
print("Rules: Rock beats scissors, scissors beat paper, and paper beats rock.")
    
user_score = 0
computer_score = 0
    
while True:
        # Get choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
        
        # Determine the winner
    result = determine_winner(user_choice, computer_choice)
        
        # Update scores
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1
        
        # Display result
    display_result(user_choice, computer_choice, result)
    print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        # Ask to play again
    if not play_again():
        print("\nThanks for playing! Final scores:")
        print(f"You: {user_score}, Computer: {computer_score}")
        break

