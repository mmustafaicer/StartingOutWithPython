# this program saves a list of numbers to a file.

def main():
    # create a list of numbers.
    numbers=[1,2,3,4,5,6,7]
    
    # open a file for writing.
    outfile=open("numberlist.txt", "w")
    
    # write the list to the file.
    for item in numbers:
        outfile.write(str(item)+"\n")   # to write on file; it should be string.
        
    # close the file.
    outfile.close()
    
# call the main function
main()