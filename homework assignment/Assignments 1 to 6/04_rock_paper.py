#Project 4: Rock, paper, scissors Python Project
#Rock, paper, scissors Python Project
#In this Kylie Ying tutorial, you will work with random.choice(), if statements, and getting user input. This is a great project to help you build on the fundamentals like conditionals and functions.

import random

def get_user_choice():
    """Get and validate user input"""
    while True:
        user_input = input("\nChoose rock, paper, or scissors: ").lower()
        if user_input in ("rock", "paper", "scissors"):
            return user_input
        print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generate computer's random choice"""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine game outcome using comparison logic"""
    if user_choice == computer_choice:
        return "tie"
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "user" if winning_combinations[user_choice] == computer_choice else "computer"

def play_game():
    """Main game loop with replay functionality"""
    print("Welcome to Rock-Paper-Scissors!")
    print("Best of luck against the computer!")
    
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        
        print(f"\nYou chose: {user.capitalize()}")
        print(f"Computer chose: {computer.capitalize()}")
        
        result = determine_winner(user, computer)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
        else:
            print("Computer wins!")
        
        if input("\nPlay again? (y/n): ").lower() != "y":
            print("\nThanks for playing!")
            break

# Start the game
play_game()