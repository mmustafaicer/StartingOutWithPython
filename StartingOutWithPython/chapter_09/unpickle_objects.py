# this program demonstrates object unpickling.
import pickle

# main function
def main():
    end_of_file= False # to indicate end of file
    
    # open a file for binary reading.
    input_file=open("info.dat", "rb")
    
    # read to the end of the file.
    while not end_of_file:
        try:
            # unpickle the next objects.
            person=pickle.load(input_file)
            
            # display the object.
            display_data(person)
        except EOFError:
            # set the flag to indicate the end
            # of file has been reached.
            end_of_file=True 
        
    # close the file.
    input_file.close()
    
# the display_data function displays the person data
# in the dictionary that is passed as an argument.

def display_data(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("Weight:", person["weight"])
    print()
    
# call the main function
main()