number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
print ("The Multiplication Table of: ", number)
for count in range(1, 13):      
   print (number, 'x', count, '=', number * count)