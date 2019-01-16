# this program uses a function to create a list.
# the function returns a reference to the list.

def main():
    # get a list with values stored in it.
    numbers=get_values()
    
    # display the values in the list.
    print("The numbers in the list are: ")
    print(numbers)
    
# the get _values function gets a series of numbers from the user and
# stores them in a list. The function returns a reference to the list.

def get_values():
    # create an empty list.
    values=[]
    
    # create a variable to control the loop.
    again="y"
    
    # get values from the user and add them to
    # the list.
    while again=="y" or again=="Y":
        # get a number and add it to the list.
        num=int(input("Enter a number: "))
        values.append(num)
        
        # want to do this again?
        print("Do you want to add another number?")
        again=input("y=yes, anything else=no: ")
        print()
    # return the list
    return values

# call the main function
main()