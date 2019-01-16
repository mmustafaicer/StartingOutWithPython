# this program uses the for loop to read
# all of the values in the sales.txt file.

def main():
    # open the sales.txt file for reading.
    sales_file=open("sales.txt", "r")
    
    # read all the lines from the file
    for line in sales_file:
        # convert line to a float.
        amount=float(line)
        # format and display the amount.
        print(format(amount, ",.2f"))
    
    # close the file
    sales_file.close()
    
# call the main function.
main()