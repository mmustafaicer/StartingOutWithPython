# this program reads numbers from a file into a list.

def main():
    # open a file for reading.
    infile=open("numberlist.txt", "r")
    
    # read the contents of the file into a list.
    numbers=infile.readlines()
    
    # close the file
    infile.close()
    
    # convert each element to an int.
    index=0
    while index<len(numbers):
        numbers[index]=int(numbers[index])
        index+=1
        
    # print the contents of the list.
    print(numbers)
    
# call the main function
main()