# this program demonstrates how the append method
# can be used to add items to a list.

def main():
    # first, create an empty list.
    name_list=[]
    
    # create a variable to control the loop.
    again="y"
    
    # add some names to the list
    while again=="y" or again=="Y":
        # get a name from the user.
        name=input("Enter a name: ")
        
        # append the name to the list.
        name_list.append(name)
        
        # add another one?
        print("Do you want to add another name?")
        again=input("y=yes, anything else=no: ")
        print()
        
    # display the names that were entered
    print("Here are the names you entered:")
    
    for name in name_list:
        print(name)
        
# call the main function
main()