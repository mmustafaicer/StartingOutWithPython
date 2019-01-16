# this program displays the contents
# of a file.

def main():
    # get the mane of a file.
    filename=input("Enter a filename: ")
    
    try:
        # open the file.
        infile=open(filename, "r")
        
        # read the file's contents
        contents=infile.read()
        
        # display the file's contents.
        print(contents)
        
        # close the file.
        infile.close()
        
    except IOError:
        print("An error occured trying to read " + \
              "the file", filename)
        
# call the main function
main()