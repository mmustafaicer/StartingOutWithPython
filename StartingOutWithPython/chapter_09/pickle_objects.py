# this program demonstrates object pickling.
import pickle 

# main function
def main():
    again='y'  # to control loop repetition.
    
    # open a file for binary writing.
    output_file=open("info.dat", "wb")
    
    # get data until the user wants to stop.
    while again.lower()=="y":
        # get data about a person and save it.
        save_data(output_file)
        
        # does the user want to enter more data?
        again=input("Enter more data? (y/n): ")
        
    # close the file.
    output_file.close()
    
# the save_data function gets data about a person,
# stores it in a dictionary, and then pickles the 
# dictionary to the specified file.

def save_data(file):
    # create an empty dictionary.
    person={}
    
    # get the data for a person and store
    # it in the dictionary.
    person["name"]=input("Name: ")
    person["age"]=int(input("Age: "))
    person["weight"]=float(input("Weight: "))
    
    # pickle the dictionary.
    pickle.dump(person, file)
    
# call the main function
main()