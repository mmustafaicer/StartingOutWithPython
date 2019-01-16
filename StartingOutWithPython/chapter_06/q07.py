# random number file writer

import random
def main():
    
    # open a file to write
    myfile=open("random_numbers.txt", "w")
    
    # ask user how many random numbers will be generated and store.
    total_numbers=int(input("How many random numbers will be generated?: "))
    
    for i in range(total_numbers):
        # produce the random number.
        # in the range of 1 through 500.
        number=random.randrange(1,501,1)
        
        # write the number to the file using \n
        myfile.write(str(number)+"\n")
    
    print("The numbers are generated and written to <random_numbers.txt>. ")
    # close the file
    myfile.close()
    
main()