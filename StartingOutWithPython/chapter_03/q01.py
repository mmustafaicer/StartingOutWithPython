# day of the week

# ask user to enter a number in the range of 1 through 7

user_number=int(input("Enter a number in the range of 1 through 7: "))

# it is better to use if-elif-else structure. Else for the outside of the range.
if user_number==1:
    print("It is Monday!")
elif user_number==2:
    print("It is Tuesday!")
elif user_number==3:
    print("It is Wednesday!")
elif user_number==4:
    print("It is Thursday!")
elif user_number==5:
    print("It is Friday!")
elif user_number==6:
    print("It is Saturday!")
elif user_number==7:
    print("It is Sunday!")
else:
    print("You entered a number that is outside the range of 1 through 7.")
