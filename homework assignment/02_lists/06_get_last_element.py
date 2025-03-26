#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[-1])

# There is no need to edit code beyond this point

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
    get_last_element(lst)

if __name__ == '__main__':
    main()
#get_last_element(lst): This function uses Python's negative indexing (lst[-1]) to directly access and print the last element of the list. This approach is efficient and concise.

#get_lst(): This function initializes an empty list and repeatedly prompts the user for elements. Each element entered is added to the list until the user presses enter without inputting text, ensuring the list is non-empty when the function returns.

#main(): This function orchestrates the process by calling get_lst() to collect the list and then passing it to get_last_element() to print the last element.