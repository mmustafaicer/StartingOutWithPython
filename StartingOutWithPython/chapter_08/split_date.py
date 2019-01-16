# this program calls the split method, using the
# "/" character as a separator.

def main():
    # create a string with a date.
    date_string="11/26/2014"
    
    # split the date.
    date_list=date_string.split("/")
    
    # display each piece of the date.
    print("Month", date_list[0])
    print("Day", date_list[1])
    print("Year", date_list[2])
    
# call the main function
main()