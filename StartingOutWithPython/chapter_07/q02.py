# lottery number generator

import random 

def main():
    numbers=random_number_generator()
    
    print("The lucky numbers are below. Thanks for participating.")
    print()
    index=0
    while index<len(numbers):
        print(numbers[index], end="  ")
        index+=1
        
def random_number_generator():
    # create an empty list
    numbers=[]
    
    # we can just use append (it will iterate 7 times)
    for i in range(7):
        numbers.append(random.randrange(0,10))
    return numbers

# call the main function
main()