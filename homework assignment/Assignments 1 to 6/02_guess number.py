#Project 2: Guess the  Number Game Python Project (computer)
#1 to 100 numbers.
import random

def guess_the_number():
    """Project 2: Guess the Number Game Python Project (computer)"""
    number = random.randint(1, 100)
    guesses_left = 7
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number:
            print("Too low. Try another!")
        elif guess > number:
            print("Too high. Try another!")
        else:
            print(f"Congratulations! You got the correct number in {7 - guesses_left + 1} guesses!")
            return

        guesses_left -= 1

    print(f"\nYou ran out of guesses. The number was {number}.")

guess_the_number()