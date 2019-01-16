# definition of the main function.
def main():
    get_name()
    print("Hello", name)        # this causes an error!

# definition of the get_name function.
def get_name():
    name=input("Enter your name: ")
    
# call the main function.
main()