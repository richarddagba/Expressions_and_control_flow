# Read integer from user input
side_length = int(input("Enter the side length of the square: "))

# Draw the square
for i in range(side_length):
    # Draw the top and bottom edges of the square
    if i == 0 or i == side_length - 1:
        print("#" * side_length)
    # Draw the left and right edges of the square
    else:
        print("#" + " " * (side_length - 2) + "#")
        

# This program first prompts the user to 
# enter an integer, which is then stored in the 
# side_length variable. The program then uses a loop to draw the 
# square, iterating through each row of the square and printing the 
# appropriate characters. The if statement checks if the current
# row is the first or last row of the square, in which case it prints 
# a row of # characters. If the current row is not the first or last row,
# the program prints a row consisting of a # character,
# followed by side_length - 2 spaces, and then another # character.
# This creates the left and right edges of the square.