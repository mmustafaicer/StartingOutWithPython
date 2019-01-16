# world series champions

def main():
    # read the WorldSeriesWinners.txt file
    infile=open("WorldSeriesWinners.txt", "r")
    
    # read the lines. eliminate \n by using splitlines()
    winners_list=infile.read().splitlines()
    
    # get the user input
    search=input("Please enter the team (first letters of each word capital): ")
    
    # calculate the total winning
    total_winning=CalculateTotalWinning(winners_list, search)
    
    # print the results.
    print()
    print("The team:", search, "has been winner", total_winning, "times.")
    
def CalculateTotalWinning(a,b): # a=list b=search_term
    # set an accumulator
    total_winning=0
    
    index=0
    while index<len(a):
        if b==a[index]:
            total_winning+=1
        index+=1
    return total_winning

# call the main function
main()