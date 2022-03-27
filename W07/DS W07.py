def countdown(num):
    if num <= 0: # check for the base
        return

    print(num) # work

    countdown(num - 1) # recursive call

## Fibonacci

number = int(input("Enter a Fibonacci index: "))

def Fib(number):

    if number <= 0:
        return
    elif number == 1:
        return 1
    elif number == 2:
        return 1
    
    return Fib(number - 1) + Fib(number - 2)

print("fib({}): {}".format(number, Fib(number)))
    
