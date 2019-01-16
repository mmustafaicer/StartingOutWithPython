# rainfall statistics

def main():
    rainfall_monthly=get_rainfall()
    
    # get the total
    index=0
    total=0.0
    while index<len(rainfall_monthly):
        total+=rainfall_monthly[index]
        index+=1
    
    print()
    print("The total rainfall is", total)
    print("The average monthly rainfall is", total/12)
    
    # get the minimum. see how we get the index of min and max values in a list.
    print("The minimum rainfall was", min(rainfall_monthly), "in the month #", end="")
    print(rainfall_monthly.index(min(rainfall_monthly))+1)
    
    # get the maximum.
    print("The minimum rainfall was", max(rainfall_monthly), "in the month #", end="")
    print(rainfall_monthly.index(max(rainfall_monthly))+1)
    
def get_rainfall():
    # create an empty list
    rainfall_monthly=[]
    
    index=0
    while index<12:
        print("Enter the total rainfall for month #", index+1, end="")
        
        # use append method to add rainfall
        rainfall_monthly.append(float(input(": ")))
        index+=1 
    # return the filled list
    return rainfall_monthly

# call the main function
main()
