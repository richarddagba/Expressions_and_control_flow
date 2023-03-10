# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
    
    # We first read an integer n from the user using the input() function and convert it to an integer using the int() function.

    # We then use a nested loop to print i asterisks on the ith row, where i ranges from 1 to n.

    # The inner loop (for j in range(1, i+1)) prints an asterisk on each column of the current row.

    # We use the end="" parameter of the print() function to suppress the newline character, so that each row is printed on the same line.

    # Finally, we use the print() function without any arguments to print a newline character after each row, so that the next row starts on a new line.