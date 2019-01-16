# sum of numbers

# ask user to enter a series of positive numbers
user_number=int(input("Enter a positive number: "))
total=0.0           # set an accumulator

while user_number>=0:
    total+=user_number
    print("Enter a positive number to continue or negative number to end ", end='')
    user_number=int(input(":"))
    
print()
print("The total of your number entered is", total)
    