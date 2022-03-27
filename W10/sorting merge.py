"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    if len(numbers) > 1:
        mid = len(numbers) // 2
        lefthalf = numbers[:mid]
        righthalf = numbers[mid:]

        sort(lefthalf) # sorting out first
        sort(righthalf) # sorting out second

        i = 0 # left half index
        j = 0 # right half index
        k = 0 # numbers index

        # the first case
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]: # if left half number is small, put in the left half number into the numbers array (main array)
                numbers[k] = lefthalf[i]
                i += 1 # go to the second left half number to compare with the right half number

            elif lefthalf[i] > righthalf[j]: #if right half number is small, put in the right half number into the numbers array(main array)
                numbers[k] = righthalf[j]
                j += 1 # go to the next right half number

            k += 1 # keep increase the numbers array (main array) for the next number to come in

        # the second case. When the right half finished early. Fill up already sorted out left half into the numbers array(main array)
        while i < len(lefthalf):
            numbers[k] = lefthalf[i]
            i += 1
            k += 1

        # the seconde - 1 case. When the left half finished early, which mean that left half numbers were smaller the the right half
        while j < len(righthalf):
            numbers[k] = righthalf[j]
            j += 1
            k += 1
    

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