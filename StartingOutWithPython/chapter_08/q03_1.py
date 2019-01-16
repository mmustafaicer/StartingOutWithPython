# import datetime library
from datetime import datetime

# get the date from the user
date_input = input('Enter a date(mm/dd/yyyy): ')

# strip the time as month, day, year
date_object = datetime.strptime(date_input, '%m/%d/%Y')

# print the full month name (%B), day and year.
print(date_object.strftime('%B %d, %Y'))
