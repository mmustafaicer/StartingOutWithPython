# this program prompts the user for sales amounts
# and writes those amounts to the sales.txt file

def main():
    # get the number of days.
    num_days=int(input("For how many days do you have sales?: "))
    
    # open a new file named sales.txt
    sales_file=open("sales.txt", "w")
    
    # get the amount of salesfor each day and
    # write it to the file.
    for count in range(1,num_days+1):
        # get the sales for a day
        sales=float(input("Enter the sales for day #" + str(count) + ": "))
        
        # write the sales amount to the file
        sales_file.write(str(sales) + "\n")
        
    # close the file.
    sales_file.close()
    print("Data written to sales.txt")
    
# call the main function
main()