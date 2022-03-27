likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print(likes.find("t", 69, -11))
print(len(likes))
print(likes.index("t", 69))

numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

# insert a number
numbers.insert(0, 5)
print(numbers)
print()

#remove a number
numbers.remove(2348)
print(numbers)
print()

"""
number1 = [66, 76, 88, 99]
numbers.append(number1)
print(numbers)
print()
"""
# extend a new list
number1 = [66, 76, 88, 99]
numbers.extend(number1)
print(numbers)
print()

# sorting
numbers.sort()
print(numbers)
print()

# find a index number
numbers.index(96)
print(numbers.index(96))
print()

# slicing into two different list
mid = len(numbers) // 2
numbers_left = numbers[:mid]
numbers_right = numbers[mid:]
print(numbers_left)
print(numbers_right)
print()

# last five elements
print(numbers[len(numbers) - 5:])
print(numbers[-5:])

# copying the list
new_number = numbers[:]
print(new_number)

# sorting backward
num = sorted(numbers, reverse = True)
print(num)