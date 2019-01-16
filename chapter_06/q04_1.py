# item counter alternative version.

def main():
    try:
        # open the names.txt file in read mode.
        infile=open("names.txt", "r")

        # set an accumulator for number of names
        numbers_of_name=0.0

        # read the rest of the file
        # remember for line in infile: already reads a line. so do not write under
        # line=infile.readline() again. It will read two times in each iteration.
        for line in infile:
            numbers_of_name+=1

        # print the numbers of names in the names.txt file.    
        print("There are ", int(numbers_of_name), "names in the names.txt file.")

        # close the file
        infile.close()
    except IOError as err:
        print (err) 

# call the main function
main()