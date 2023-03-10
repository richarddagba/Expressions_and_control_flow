# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

import random

stored_number = random.randint(1, 10)  # generate a random number between 1 and 10

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    
    if guess < stored_number:
        print("The stored number is higher.")
    elif guess > stored_number:
        print("The stored number is lower.")
    else:
        print("You found the number:", stored_number)
        break

# The random.randint() function generates a random integer between the specified range of 1 and 10, inclusive, and stores it in the stored_number variable.

# The while loop runs indefinitely until the user correctly guesses the number.

# Inside the loop, the program asks the user to enter a guess using the input() function and converts it to an integer using the int() function.

# If the guess is less than the stored number, the program prints "The stored number is higher."

# If the guess is greater than the stored number, the program prints "The stored number is lower."

# If the guess is equal to the stored number, the program prints "You found the number:" followed by the actual stored number, and the break statement exits the loop