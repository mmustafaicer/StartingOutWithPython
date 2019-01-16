# this program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # initialize an accumulator.
    total=0.0
    
    try:
        # open the sales_data.txt file.
        infile=open("sales_data.txt", "r")
        
        # read the values from the file
        # and accumulate them.
        for line in infile:
            amount=float(line)
            total+=amount 
            
        # close the file.
        infile.close()
        
    except Exception as err:
        print(err)
    else:
        # print the total.
        print(format(total, ",.2f"))
        
# call the main function.
main()