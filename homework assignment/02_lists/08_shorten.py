MAX_LENGTH: int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()

#Function shorten(lst):

#This function takes a list as an argument.

#It uses a while loop to check if the length of the list exceeds MAX_LENGTH (which is set to 3).

#For each iteration, the last element of the list is removed using pop() and printed.

#The loop continues until the list's length is reduced to MAX_LENGTH.

#Function get_lst():

#This helper function prompts the user to input elements one by one, building the list until the user inputs a blank line.

#Function main():

#This function orchestrates the process by first calling get_lst() to obtain the list from the user and then passing the list to shorten() to process it.    