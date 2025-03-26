def get_user_numbers():
    """
    Collects numbers entered by the user into a list. 
    Handles invalid inputs and stops when a blank line is entered.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ").strip()
        
        if user_input == "":
            break
            
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print(f"⚠️ '{user_input}' is not a valid number. Skipping...")
    
    return user_numbers

def count_nums(num_lst):
    """Counts occurrences of each number (unchanged from original solution)"""
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def print_counts(num_dict):
    """Prints counts (unchanged from original solution)"""
    for num, count in num_dict.items():
        print(f"{num} appears {count} time{'s' if count != 1 else ''}.")

def main():
    """Main function (unchanged structure)"""
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()