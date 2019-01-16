# this program displays five random
# numbers in the range of 1 through 100
import random

def main():
    for count in range(5):
        print(random.randint(1,100))

# call the main function
main()