# this program allows the user to modify the quantity
# in a record in the coffee.txt file.

import os # needed for the remove and rename functions

def main():
    # create a bool variable to use as a flag.
    found=False 
    
    # get the search value and the new quantity
    search=input("Enter a description to search for: ")
    new_qty=int(input("Enter the new quantity: "))
    
    # open the original coffee.txt file.
    coffee_file=open("coffee.txt", "r")
    
    # open a temporary file.
    temp_file=open("temp.txt", "w")
    
    # read the first record's description field.
    descr=coffee_file.readline()
    
    # read the rest of the file
    while descr!="":
        # read the quantity field.
        qty=float(coffee_file.readline())
        
        # strip the \n from the description
        descr=descr.rstrip("\n")
        
        # write either this record to temporary file
        # or the new record if this is the one that is
        # to be modified
        if descr==search:
            # write the modified record to the temp file.
            temp_file.write(descr+"\n")
            temp_file.write(str(new_qty)+"\n")
            
            # set the found flag to True.
            found=True 
        else:
            # write the original record to the temp file.
            temp_file.write(descr+"\n")
            temp_file.write(str(qty)+"\n")
        
        # read the next description
        descr=coffee_file.readline()
        
    # close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()
    
    # delete the original coffee.txt file.
    os.remove("coffee.txt")
    
    # rename the temporary file
    os.rename("temp.txt", "coffee.txt")
    
    # if the search value was not found in the file 
    # display a message.
    if found:
        print("The file has been updated.")
    else:
        print("The item was not found in the file.")

# call the main function
main()

            