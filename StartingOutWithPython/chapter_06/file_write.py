# this program writes three lines of data
# to a file.
def main():
    # open a file named philosophers.txt
    # it will be in the same folder as of Python file.
    outfile=open("philosophers.txt", "w")
    
    # write the names of three philosophers
    # to the file
    outfile.write("John Locke\n")       # \n for new line
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")
    
    # close the file
    outfile.close()
    
# call the main function
main()