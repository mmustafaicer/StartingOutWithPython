# file head display shorter version

def main():
    
    # ask user to enter a filename.
    filename=input("Enter the file name: ")
    
    # open that file name
    infile=open(filename, "r")
    
    # read the 5 lines from the file.
    for i in range(5):
        line=infile.readline()
        line=line.rstrip("\n")
        print(line)
    
    # close the file.
    infile.close()
    
# call the main function
main()