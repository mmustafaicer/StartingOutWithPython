# this program demonstrates how numbers that are read
# from a file must be converted from strings before
# they are used in a math operation

def main():
    # open a file for reading.
    infile=open("numbers.txt", "r")
    
    # read the three numbers from the file.
    num1=int(infile.readline())
    num2=int(infile.readline())
    num3=int(infile.readline())
    
    # close the file
    infile.close()
    
    # add the three numbers.
    total=num1+num2+num3
    
    # display the numbers and their total.
    print("The numbers are:", num1, num2, num3)
    print("Their total is", total)
    
# call the main function
main()