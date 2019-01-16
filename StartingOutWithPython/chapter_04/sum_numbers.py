# this program calculates the sum of a series
# of numbers entered by the user.

max_num=5 # maximum number.
# initialize an accumulator variable.
total=0.0

# explain what we are doing
print("This program calculates the sum of")
print(max, "numbers you will enter.")

# get the numbers and accumulate them
for counter in range(max_num):
    number=int(input("Enter a number: "))
    total=total+number
    
# display the total of the numbers.
print("The total is", total)