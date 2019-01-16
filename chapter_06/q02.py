# file head display
# for a shorter alternative check q02_1.py

def main():
    
    # ask user to enter a filename.
    filename=input("Enter the file name: ")
    
    # open that file name
    infile=open(filename, "r")
    
    # read the 5 lines from the file.
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    line4=infile.readline()
    line5=infile.readline()
    
    # strip the \n s from end.
    line1=line1.rstrip("\n")
    line2=line2.rstrip("\n")
    line3=line3.rstrip("\n")
    line4=line4.rstrip("\n")
    line5=line5.rstrip("\n")
    
    # print the contents
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    
    # close the file.
    infile.close()
    
# call the main function
main()