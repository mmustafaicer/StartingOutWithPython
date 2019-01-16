# population data

def main():
    # read the population file
    pop_file=open("USPopulation.txt", "r")
    
    # read the lines
    pop_list=pop_file.readlines()
    
    # read each line as an integer
    index=0
    while index<len(pop_list):
        pop_list[index]=int(pop_list[index])
        index+=1
    
    # calculate annual change
    annual_change=AnnualChange(pop_list)
    
    # calculate the total of annual change
    total=0
    for y in annual_change:
        total+=y
        
    # calculate the average
    average=total/len(annual_change)
    
    print("The average annual change in population between 1950 and 1990 is", format(average, ",.2f"))
    print("The greatest increase in population occured in the year of", annual_change.index(max(annual_change))+1951,"with an increase of", max(annual_change))
    print("The smallest increase in population occured in the year of", annual_change.index(min(annual_change))+1951, "with an increase of", min(annual_change))
    
    # if you want to print yearly annual change data
    print()
    print("Years\t\tAnnual Change")
    print("-----------------------------")
    for i in range(1,41,1):
        print(i+1950, "-", i+1949 , "\t\t", annual_change[i-1], sep="")
        
          
def AnnualChange(pop_list):
    # create an empty list
    annual_change=[0]*(len(pop_list)-1)
    
    # calculate annual change. Example (year 2 - year 1)
    index=0
    
    # since there are 41 years, there will be 40 annual change
    # excluding first year.
    while index<len(pop_list)-1:
        annual_change[index]= pop_list[index+1]-pop_list[index]
        index+=1    
    return annual_change    
    
# call the main function
main()