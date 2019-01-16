# total sales

def main():
    sales=get_sales()
    total=get_total(sales)
    print()
    print("Total sales is $", total, sep='')
    
def get_sales():
    # create an empty list with 7 days.
    sales=[0]*7
    
    index=0
    # ask user to enter sales for each day of a week.
    while index<len(sales):
        print("Please enter the sales for day #", index+1, sep="", end='')
        sales[index]=float(input(": "))
        index+=1
    
    # return the list    
    return sales

def get_total(sales):
    # create an accumulator
    total=0
    index=0
    while index<len(sales):
        total+=sales[index]
        index+=1
        
    return total    

# call the main function
main()