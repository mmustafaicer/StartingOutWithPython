# this program creates five CellPhone objects and
# stores them in a list.

import cellphone

def main():
    # get a list of CellPhone objects.
    phones=make_list()
    
    # display the data in the list.
    print("Here is the data that you entered: ")
    display_list(phones)
    
# the make_list function gets data from the user.
# for five phones. The function returns a list of
# CellPhone objects containing the data.
def make_list():
    # create an empty list.
    phone_list=[]
    
    # add five CellPhone objects to the list.
    print("Enter data for five phones.")
    print()
    for count in range(1,6):
        # get the phone data.
        print("Phone number ", str(count), ":", sep="")
        man=input("Enter the manufacturer: ")
        mod=input("Enter the model number: ")
        retail=float(input("Enter the retail price: "))
        print()
        
        # create a new CellPhone object in memory and
        # assign it to the phone variable.
        phone=cellphone.CellPhone(man,mod,retail)
        
        # add the object to the list.
        phone_list.append(phone)
    # return the list
    return phone_list

# the display_list function accepts a list containing
# CellPhone objects as an argument and displays the
# data stored in each object.
def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()
        
# call the main function
main()
        