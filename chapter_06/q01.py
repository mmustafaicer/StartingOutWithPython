# file display

def main():
    
    # open the numbers.txt file. Make sure it exists.
    myfile=open("numbers.txt", "r")
    
    # this loop reads every line on that file.
    for line in myfile:
        line=float(line)
        print(line)
    
    # close the file
    myfile.close()
    
# call the main function
main()