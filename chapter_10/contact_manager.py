# this program manages contacts.
import contact
import pickle
from lib2to3.tests.data.infinite_recursion import FILE

# global constants for menu choices.
LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

# global constant for the filename.
FILENAME="contacts.dat"

# main function
def main():
    # load the existing contact dictionary and
    # assign it to mycontacts.
    mycontacts=load_contacts()
    
    # initialize a variable for the user's choice.
    choice=0
    
    # process menu selections until user 
    # wants to quit the program
    while choice!=QUIT:
        # get the user's menu choice.
        choice=get_menu_choice()
        
        # process the choice.
        if choice==LOOK_UP:
            look_up(mycontacts)
        elif choice==ADD:
            add(mycontacts)
        elif choice==CHANGE:
            change(mycontacts)
        elif choice==DELETE:
            delete(mycontacts)
            
    # save the mycontacts dictionary to a file
    save_contacts(mycontacts)
    
def load_contacts():
    try:
        # open the contacts.dat file.
        input_file=open(FILENAME, "rb")
        
        # unpickle the dictionary.
        contact_dct=pickle.load(input_file)
        
        # close the contacts.dat file
        input_file.close()
        
    except IOError:
        # could not open the file, so create
        # an empty dictionary.
        contact_dct={}
        
    # return the dictionary.
    return contact_dct

# the get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print("Menu")
    print("-------------------")
    print("1. Look up a contact")
    print("2. Add a new contact")
    print("3. Change an existing contact.")
    print("4. Delete a contact.")
    print("5. Quit the program.")
    print()
    
    # get the user's choice.
    choice=int(input("Enter your choice: "))
    
    # validate the choice.
    while choice<LOOK_UP or choice>QUIT:
        choice=int(input("Enter a valid choice: "))
    
    # return the user's choice.
    return choice

# the look_up function looks up an item in the
# speficied dictionary.
def look_up(mycontacts):
    # get a name to look up.
    name=input("Enter a name: ")
    
    # look it up in the dictionary.
    print(mycontacts.get(name, "That name is not found."))
    
# the add function adds a new entry into the 
# specified dictionary.
def add(mycontacts):
    # get the contact info.
    name=input("Name: ")
    phone=input("Phone: ")
    email=input("Email: ")
    
    # create a Contact object named entry.
    entry=contact.Contact(name,phone,email)
    
    # if the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in mycontacts:
        mycontacts[name]=entry
        print("The entry has been added.")
    else:
        print("That name already exists.")
        
# the change function changes an existing
# entry in the specified dictionary.

def change(mycontacts):
    # get a name to look up.
    name=input("Enter a name: ")
    
    if name in mycontacts:
        # get a new phone number.
        phone=input("Enter the new phone number: ")
        
        # get a new email address.
        email=input("Enter the new email address: ")
        
        # create a contact object named entry
        entry=contact.Contact(name,phone,email)
        
        # update the entry.
        mycontacts[name]=entry
        print("Information updated.")
    else:
        print("That name is not found.")
        
# the delete function deletes an entry from the 
# specified dictionary.

def delete(mycontacts):
    # get a name to look up.
    name=input("Enter a name: ")
    
    # if the name is found, delete the entry
    if name in mycontacts:
        del mycontacts[name]
        print("Entry deleted!")
    else:
        print("That name is not found.")
        
# the save_contacts function pickles the specified
# object and saves it to the contacts file.

def save_contacts(mycontacts):
    # open the file for writing.
    output_file=open(FILENAME, "wb")
    
    # pickle the dictionary and save it.
    pickle.dump(mycontacts, output_file)
    
    # close the file.
    output_file.close()

# call the main function
main()