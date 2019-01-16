# this program reads the contents of the 
# philosophers.txt file one line at a time.

def main():
    # open a file named philosophers.txt.
    infile=open("philosophers.txt", "r")
    
    # read the three lines from the file
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    
    # strip the \n from each string
    line1=line1.rstrip("\n")
    line2=line2.rstrip("\n")
    line3=line3.rstrip("\n")
    
    # close the file.
    infile.close()
    
    # print the data that was read into 
    # memory
    print(line1)
    print(line2)
    print(line3)
    
# call the main function
main()