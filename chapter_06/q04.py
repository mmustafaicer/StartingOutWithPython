# item counter
# there is an alternative version with for loop.

def main():
    try:
        # open the names.txt file in read mode.
        infile=open("names.txt", "r")
        
        # set an accumulator for number of names
        numbers_of_name=0.0
        
        # read the first line
        line=infile.readline()
        
        # read the rest of the file
        while line!="":
            numbers_of_name+=1
            line=infile.readline()
            
        # print the numbers of names in the names.txt file.    
        print("There are", int(numbers_of_name), "names in the names.txt file.")
        
        # close the file
        infile.close()
    except IOError as err:
        print (err) 
        
# call the main function
main()