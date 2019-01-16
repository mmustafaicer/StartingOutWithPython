# average of numbers

def main():
    try:
        # open the file
        infile=open("numbers.txt", "r")
        
        # set an accumulator for number of files and total
        total_numbers=0.0
        total=0.0
        
        # read the file and calculate average
        for line in infile:
            line=float(line)
            total+=line
            total_numbers+=1
            
        # calculate the average
        average=total/total_numbers
        print("There are" ,int(total_numbers), "numbers in the <numbers.txt>. And their average is", average)
        
        # close the file
        infile.close()
    # in case there are 0 numbers in the file. it can't be divided by zero.   
    except ZeroDivisionError:
        print("ERROR: There are no numbers in the file.")
    
    # in case there are non-numeric lines in the file.
    except ValueError:
        print("ERROR: There are non-numeric lines in the file.")
        
    
# call the main function.
main()