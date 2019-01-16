# this program demonstrates the sqrt function.
import math

def main():
    # get a number.
    number=float(input("Enter a number: "))
    
    # get the square root of the number.
    square_root=math.sqrt(number)
    
    # display the square root.
    print("The square root of", number, "is", format(square_root, ",.1f"))
    
# call the main function
main()