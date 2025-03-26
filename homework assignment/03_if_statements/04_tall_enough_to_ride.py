MINIMUM_HEIGHT : int = 50  # arbitrary units :)

def main():
    while True:
        height_input = input("How tall are you? ")
        
        # If the user enters an empty string, stop the loop
        if height_input == "":
            break
        
        # Try to convert the input to a float (height) and handle any invalid input
        try:
            height = float(height_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for your height.")
    
    print("Thanks for checking your height! Goodbye!")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
