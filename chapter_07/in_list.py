# this program demonstrates the in operator
# used with a list.

def main():
    # create a list of product numbers.
    prod_nums=["V475", "F987", "Q143", "R688"]
    
    # get a product number to search for.
    search=input("Enter a product number: ")
    
    # determine whether the product number is in the list.
    if search in prod_nums:             # it returns True if found in the list.
        print(search, "was found in the list.")
    else:
        print(search, "was not found in the list.")
        
# call the main function
main()