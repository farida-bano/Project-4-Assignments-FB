import random

def main():
    # Generate the secret number at random between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Initial guess prompt
    guess = int(input("Enter a guess: "))

    # Loop until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Prompt the user for another guess
        print()  # Print an empty line to tidy up the console for new guesses
        guess = int(input("Enter a new guess: "))
    
    # Congratulate the user when they guess correctly
    print(f"Congrats! The number was: {secret_number}")

# This required line calls the main() function to run the game
if __name__ == '__main__':
    main()
