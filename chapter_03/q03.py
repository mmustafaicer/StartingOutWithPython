# age classifier

# ask user to enter an age

age=int(input("Please enter your age: "))

# determine the category of age

if age<=1 and age>0:
    print("The category is infant!")
elif age>1 and age<13:
    print("The category is child!")
elif age>=13 and age<20:
    print("The category is teenager!")
elif age>=20:
    print("The category is adult!")
else:       # in case user enters a number less than 0, it will give an error. Age can't be 0 and less than 0.
    print("The age you entered is not valid.")