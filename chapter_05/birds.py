# this program demonstrates two functions that
# have local variables with the same name.

def main():
    # call the texas function.
    texas()
    # call the california function
    california()

# definition of the texas function. it creates
# a local variable named birds.
def texas():
    birds=5000
    print("Texas has", birds, "birds.")

#definition of the california function. it also 
# creates a local variable named birds.
def california():
    birds=8000
    print("California has", birds, "birds.")

# call the main function
main()