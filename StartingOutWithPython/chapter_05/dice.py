# this program shows the rolling of dice
import random

# constants for the min and max random numbers.
MIN=1
MAX=6

def main():
    # create a variable to control the loop
    again='y'
    # simulate the rolling the dice
    while again=="y" or again=="Y":
        print("Rolling the dice ...")
        print("Their values are:")
        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))
        
        # do another roll of the dice?
        again=input("Roll them again? (y=yes): ")
        print()
        
# call the main function
main()
        