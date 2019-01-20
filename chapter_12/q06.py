# sum of numbers

def main():
    # set beginning point
    beg=1
    
    # get the data from the user
    end=int(input("Enter a positive integer: "))
    print()
    
    # call the function
    total=sum_num(beg, end)
    
    # display the result.
    print("The total of the numbers from 1 up to", end, "equals to", total)
    
def sum_num(beg, end):
    if beg<=end:
        return beg + sum_num(beg+1, end)
    else:
        return 0
    
    # alternative
    #===========================================================================
    # # or
    # if beg<end:
    #     return beg + sum_num(beg+1, end)
    # else:
    #     return beg
    #===========================================================================
    
# call the main function
main()