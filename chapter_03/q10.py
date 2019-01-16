# money counting game

# get the number of pennies, nickels, dimes, and quarters.

penny=int(input("Enter the amount of pennies: "))
nickel=int(input("Enter the amount of nickels: "))
dime=int(input("Enter the amount of dimes: "))
quarter=int(input("Enter the amount of quarters: "))

# create decision structure to see if that equals to $1. Remember $1 is 100 cents.
print()
total=penny+5*nickel+10*dime+25*quarter

if total==100:
    print("Congratulations. It equals to $1.")
elif total<100:
    print("Sorry! It is less than $1.")
else:
    print("Sorry! It is more than $1.")