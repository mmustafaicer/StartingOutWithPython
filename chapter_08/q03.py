# date printer
# there is an alternative version using builtin library

def main():
    # get the date from the user.
    date=get_date()
    
    # convert date to like March 12, 2014
    literal_date=convert(date)
    
    print("The date is below.")
    print(literal_date)
    
def get_date():
    date=input("Enter the date as mm/dd/yyyy: ")
    return date

def convert(date):
    # first separate the string.
    date_list=date.split("/")
    
    # create a list for months.
    months=["January", "February", "March", "April", "May", \
            "June", "July", "August", "September", "October", \
            "November", "December"]
    
    # lets concatenate each value.
    # if month is entered as 01 it should be January. But January's index is 0.
    # that is why int(date_list[0]-1)
    new_date=str(months[int(date_list[0])-1]) + " " + str(date_list[1]) + "," + " " + str(date_list[2])
    return new_date
    
# call the main function
main()
    
    