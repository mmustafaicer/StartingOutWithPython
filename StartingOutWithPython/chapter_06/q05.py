# sum of numbers

def main():
    try:
        # read the file.
        myfile=open("numbers.txt", "r")
        
        # set an accumulator for total
        total=0.0
        
        # read all the lines from the file
        for line in myfile:
            # the line is always string. convert it to float
            line=float(line)
            total+=line 
            
        # print the total
        print("The total of the numbers in the file <numbers.txt> is", total)
            
        # close the file
        myfile.close()
        
        # in case one of the lines is not numeric. Such as "xyz".
    except ValueError:
        print("ERROR: At least one of the lines in the file <numbers.txt> is not numeric.")
        
    
# call the main function.
main()