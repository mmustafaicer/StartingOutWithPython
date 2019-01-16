# calculating the factorial of a number

# ask user to enter a nonnegative number
user_number=int(input("Enter a nonnegative integer to calculate factorial: "))

# set an accumulator
factorial=1

# check if user entered a negative number and prompt user to enter again.
while user_number<0:
    user_number=int(input("ERROR: Please enter a positive number."))
  
# factorial part.    
for n in range(1,user_number+1, 1):
    factorial*=n
print()
print("Factorial of", user_number, "is", factorial)

