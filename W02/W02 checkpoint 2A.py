def positive():
    a = -1
    while a < 0:
        a = int(input("Enter a positive number: "))
        if a < 0:
            print("Invalid entry. The number must be positive")
        else:
            print()
            return a

def summation(x, y, z):
    return x + y + z

def main():
    x = positive()
    y = positive()
    z = positive()
    result = summation(x, y, z)
    print("The sume is: ", result)

if __name__ == "__main__":
    main()