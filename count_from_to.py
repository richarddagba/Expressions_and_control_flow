first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if second_num <= first_num:
    print("The second number should be bigger")
else:
    for i in range(first_num, second_num+1):
        print(i)