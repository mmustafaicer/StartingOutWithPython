# random number file reader

def main():
    
    # open the file to read
    myfile=open("random_numbers.txt", "r")
    
    # set accumulators
    total=0.0
    numbers=0.0
    print("The numbers in the file as follows:")
    print()
    
    # read the contents of the file.
    for line in myfile:
        line=float(line)
        print(line)
        total+=line
        numbers+=1
        
    # print the results.
    print()
    print("There are", int(numbers), "numbers in the <random_numbers.txt> file.")
    print("And their total is", total)
    
# call the main function.
main()