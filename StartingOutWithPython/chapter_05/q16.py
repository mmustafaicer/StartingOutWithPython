# odd/even counter

import random

def main():
    # lets set a counter/tracker for odd and even numbers
    total_odd_numbers=0
    total_even_numbers=0
    
    # program asks for 100 random numbers. So set a for loop.
    # change 100 to 5 to see if it is working correctly. 
    for n in range(100):
        number=GenerateRandomNumbers()
        if number%2==0:
            total_even_numbers+=1
        elif number%2==1:
            total_odd_numbers+=1
    print("There are", total_even_numbers, "even numbers and", total_odd_numbers, "odd numbers in the list.")
    
def GenerateRandomNumbers():
    # do not forget to pass arguments to random.randint(). otherwise it will give error
    # like we passed 0,1000
    number=random.randint(0,1000)
    print(number)
    return number

main()