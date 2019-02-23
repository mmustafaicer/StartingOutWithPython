# world series winners

# there was one line missing in the original
# WorldSeriesWinners.txt
# I added Toronto Blue Jays for year 1993

def main():
    # read the WorldSeriesWinners.txt file.
    myfile=open("WorldSeriesWinners.txt", "r")
    
    # read the lines by eliminating "\n"
    lines=myfile.read().splitlines()
    
    # close the file
    myfile.close()
    
    # create dictionaries for 
    num_times_dict={}
    winner_dict={}
    
    # populate first dictionary. KEY: name of teams. 
    # VALUE: number of times that team has won.
    count=1
    for teams in lines:
        if teams not in num_times_dict:
            num_times_dict[teams]=count
        else:
            num_times_dict[teams]+=1
            
    # populate the second dictionary. KEY: years VALUE: name of the team that year
    year=1903
    for teams in lines:
        winner_dict[year]=teams
        year+=1
    
    # ask user to enter a year
    keep_going="y"
    while keep_going=="y" or keep_going=="Y":
        year=int(input("Please enter a year: "))
        if year>=1903 and year<=2008 and year!=1904 and year!=1994:
            print("The winner that year is", winner_dict[year], "and it has won the cup", num_times_dict[winner_dict[year]], "times.")
        elif year==1904 or year==1994:
            print("World series was not played in this year.") 
        else: 
            print("ERROR: Please enter a valid year between 1903 through 2008.")
        keep_going=input("You want to continue? (y/n): ")
        print()       
        
# call the main function
main()