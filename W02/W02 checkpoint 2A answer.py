def prompt_number():
    number = -1
    while number < 0:
        number_str = input("Enter a positive number: ")
        number = int(number_str)
        if number < 0:
            print("Invalid entery. The number must be positive.")
    print()
    return number

def compute_number(number1, number2, number3):
    return number1 + number2 + number3


def main():
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()
    sum = compute_number(num1, num2, num3)
    print("The sum is: {}" .format(sum))

if __name__ == "__main__":
    main()