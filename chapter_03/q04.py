# roman numerals

# ask user for a number within the range of 1 through 10

number=int(input("Please enter a number within the range of 1 through 10: "))

# display the roman version

if number==1:
    print("I")
elif number==2:
    print("II")
elif number==3:
    print("III")
elif number==4:
    print("IV")
elif number==5:
    print("V")
elif number==6:
    print("VI")
elif number==7:
    print("VII")
elif number==8:
    print("VIII")
elif number==9:
    print("IX")
elif number==10:
    print("X")
else:
    print("ERROR: You entered a number outside the range of 1 through 10!")
