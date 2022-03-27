import random
from random import randint

print("Welcome to the \"1 ~ 100\" random guessing game!")
my_seed = input("Enter random seed: ")
random.seed(my_seed)  #seed(): save the state of random function

ans = "yes"
name = input("Enter your name: ")

while ans == "yes":
    rand = randint(1, 100)
    count = 0
    print()
    guess = 0 # entering to the next while loop # 2nd submission
    #guess = int(input("please enter a guess: "))  # 1st submission
    while guess != rand:
        guess = int(input("please enter a guess: ")) #2nd submission
        if guess > rand:
            print("Lower")
            print()
            count += 1 # counting guessing number of times
            #guess = int(input("please enter a guess: ")) # 1st submission # makes run while loop again by changes the guess number
        elif guess < rand:
            print("Higher")
            print()
            count += 1
            #guess = int(input("please enter a guess: ")) # 1st submission #changes the guess number
    count += 1  # from this line, coming out from the while loop 2 when guessing is right
    print()
    print("Congratulation {}! You guessed it!".format(name))
    print("It took you {} guesses." .format(count))
    print()
    ans = input("Would you like to play again (yes/no)?: ") # deciding for while loop 1
print()
print("Thank you. Goodbye.")
