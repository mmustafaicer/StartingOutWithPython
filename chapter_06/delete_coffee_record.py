# this program allows the user to delete
# a record in the coffee.txt file.

import os   # needed for the remove and rename functions

def main():
    # create a bool variable to use as flag.
    found=False
    
    # get the coffee to delete.
    search=input("Which coffee do you want to delete?: ")
    
    # open the original coffee.txt file.
    coffee_file=open("coffee.txt", "r")
    
    # open the temporary file.
    temp_file=open("temp.txt", "w")
    
    # read the first record's description field.
    descr=coffee_file.readline()
    
    # read the rest of the file.
    while descr!="":
        # read the quantity field
        qty=float(coffee_file.readline())
        
        # strip the \n from the description
        descr=descr.rstrip("\n")
        
        # if this is not the record to delete, 
        # then write it to the temporary file
        
        if descr!=search:
            # write he record to the temp file.
            temp_file.write(descr+"\n")
            temp_file.write(str(qty)+"\n")
            
        else:
            # set the found flag to True.
            found=True 
        
        # read the next description.
        descr=coffee_file.readline()
        
    # close the coffee file and temporary file.
    coffee_file.close()
    temp_file.close()
    
    # delete the original coffee.txt file
    os.remove("coffee.txt")
    
    # rename the temporary file.
    os.rename("temp.txt", "coffee.txt")
    
    # if the search value was not found in the file
    # display a message.
    
    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file.")
        
# call the main function
main()
    
            