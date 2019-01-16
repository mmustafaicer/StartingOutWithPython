# line numbers

def main():
    
    # set an line indicator starting from 1.
    line_numbering=1
    
    # ask user to enter a file name.
    filename=input("Enter a file name to open: ")
    print()
    
    # open the file
    userfile=open(filename, 'r')
    
    # read every line and print with the line number
    for line in userfile:
        # lets print the line numbers with semi colon. 
        # but it will not end with new line. so end=""
        print(line_numbering, ": ", sep="", end='')
        
        # print each number with stripping \n
        print(line.rstrip("\n"))
        
        # increase the line numbering by one.
        line_numbering+=1
    
    # close the file.
    userfile.close()
    
# call the main function
main()
    