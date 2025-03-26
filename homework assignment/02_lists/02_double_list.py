def main():
    numbers = [1, 2, 3, 4]  # Creates the initial list of numbers

    for i in range(len(numbers)):  # Iterate over each index in the list
        numbers[i] = numbers[i] * 2  # Double the element at the current index

    print(numbers)  # Output the modified list


if __name__ == '__main__':
    main()