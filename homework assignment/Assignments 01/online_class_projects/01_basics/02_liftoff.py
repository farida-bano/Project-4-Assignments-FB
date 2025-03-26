def main():
    # Using a for loop to countdown from 10 to 1
    for i in range(10, 0, -1):  # Start at 10, stop at 1, step by -1
        print(i, end=" ")  # Print the number followed by a space
    
    # Print "Liftoff!" after the countdown
    print("Liftoff!")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
