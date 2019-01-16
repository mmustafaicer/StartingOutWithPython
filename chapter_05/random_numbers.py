# this program displays a random number
# in the range of 1 through 10.
import random

def main():
    # get a random number.
    number=random.randint(1,10)
    # display the number
    print("The number is", number)

# call the main function
main()