# this program uses recursion to calculate
# the factorial of a number.

def main():
    # get a number from the user.
    number=int(input("Enter a nonnegative integer: "))
    
    # get the factorial of the number.
    fact=factorial(number)
    
    # display the factorial.
    print("The factorial of", number, "is", fact)
    
# the factorial function uses recursion to
# calculate the factorial of its argument,
# which is assumed to be nonnegative.
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    
# call the main function.
main()