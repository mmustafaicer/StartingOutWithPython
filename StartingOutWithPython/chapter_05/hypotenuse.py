# this program calculates the length of a right 
# triangle's hypotenuse.
import math

def main():
    # get the length of the triangle's two sides
    a=float(input("Enter the length of side A: "))
    b=float(input("Enter the length of side B: "))
    
    # calculate the length of the hypotenuse.
    c=math.hypot(a, b)
    
    # display the length of the hypotenuse.
    print("The length of the hypotenuse is", c)

# call the main function
main()