"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    for index in range(1, len(numbers)): # starting with index 1 because it will compare with index 0 too
        comparing_value = numbers[index] # entering value that will be compared until it finds its place
        position = index # record its index number

        while position > 0 and numbers[position - 1] > comparing_value:
            numbers[position] = numbers[position - 1] #  bigger lower index value will be recorded on the right place
            position -= 1 # To move from right to the left

        numbers[position] = comparing_value # when position becomes zero or comparing_value is the biggest to the lower level index numbers
                                            # that decreased position is the comparing-value


# Much easier way
"""
for sort_pos in range(1, len(numbers)):
 # Find swapping each pair starting from sort_pos to 1
    for swap_pos in range(sort_pos, 0, -1):
 # Compare swap_pos and swap_pos-1
        if numbers[swap_pos] < numbers[swap_pos-1]:
 # Swap if needed
            numbers[swap_pos], numbers[swap_pos-1] = numbers[swap_pos-1], numbers[swap_pos]
"""

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()