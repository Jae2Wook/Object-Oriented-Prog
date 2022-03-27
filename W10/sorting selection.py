"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    for rightspace in range(len(numbers) - 1 , 0 , -1): # filling in from the right to the left. The last index number is length - 1. Come down to 1
        max_index = 0 # scanning from the left
        for left_to_right in range(1, rightspace + 1): # starting scanning from index number 1
            if numbers[left_to_right] > numbers[max_index]:
                max_index = left_to_right # Get the maximun number's index number
            numbers[rightspace], numbers[max_index] = numbers[max_index], numbers[rightspace] # change with the right space and the maximum number space
    

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