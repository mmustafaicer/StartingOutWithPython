# this program uses the return value of a function.

def main():
    # get the user's age.
    first_age=int(input("Enter your age: "))
    
    # get the user best friend's age.
    second_age=int(input("Enter your best friend's age: "))
    
    # get the sum of both ages
    total=sum(first_age, second_age)
    
    # display the total age.
    print("Together you are", total, "years old.")
    
# the sum function accepts two numeric arguments and
# returns the sum of those arguments
def sum(num1, num2):
    result=num1+num2
    return result
# call the main function
main()