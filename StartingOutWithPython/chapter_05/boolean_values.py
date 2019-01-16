def is_even(number):
    if (number%2)==0:
        status=True
    else:
        status=False
    return status

number=int(input("Enter a number: "))

if is_even(number):         # means that if the result of this function is True.
    print("The number is even")
else:
    print("The number is odd.")