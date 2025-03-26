#Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

#Here's a sample run (user input is in blue):

#Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    lst = []
    val = input("Enter a value: ")
    while val:
        lst.append(val)
        val = input("Enter a value: ")
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()


#Initialization: The empty list lst is created to store user inputs.

#First Input Prompt: The user is prompted to enter the first value using input("Enter a value: ").

#Loop for Continuous Input: A while loop checks if val (the user input) is non-empty. If the user enters a value, it is appended to lst, and the next input is prompted. If the user presses enter without typing, val becomes an empty string, the loop exits, and the program proceeds to print the list.

#Printing the Result: After the loop exits, the collected list is printed using print("Here's the list:", lst).    