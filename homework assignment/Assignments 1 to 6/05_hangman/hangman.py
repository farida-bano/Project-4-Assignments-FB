#Project 5: Hangman Python Project
#Hangman Python Project
#In this Kylie Ying tutorial, you will learn how to work with dictionaries, lists, and nested if statements. You will also learn how to work with the string and random Python modules.
#https://youtu.be/8ext9G7xspg?si=UpZcVPyz3674bHE9
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    words = [
        "PYTHON", "JAVA", "JAVASCRIPT", "COMPUTER", "PROGRAMMING", "DEVELOPER", 
        "HANGMAN", "ALGORITHM", "DATASTRUCTURE", "MACHINE", "LEARNING", "AI", 
        "GITHUB", "PYCHARM", "TENSORFLOW", "FLASK", "DJANGO", "VSCODE", "DEBUGGING"
    ]
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and used letters: {' '.join(used_letters)}")
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"\nLetter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("\nYou've already used that letter. Try another one.")
        else:
            print("\nInvalid character. Please try again.")

    if lives == 0:
        print(f"You died! The word was {word}")
    else:
        print(f"Congratulations! You guessed the word {word}!")

if __name__ == '__main__':
    hangman()
