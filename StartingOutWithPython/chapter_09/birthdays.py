# this program uses a dictionary to keep friends'
# names and birthdays.

# global constants for menu choices.
LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

# main function
def main():
    # createa an empty dictionary.
    birthdays={}
    
    # initialize a variable for the user's choice.
    choice=0
    
    while choice!=QUIT:
        # get the user's menu choice.
        choice=get_menu_choice()
        
        # process the choice
        if choice==LOOK_UP:
            look_up(birthdays)
        elif choice==ADD:
            add(birthdays)
        elif choice==CHANGE:
            change(birthdays)
        elif choice==DELETE:
            delete(birthdays)
    
    # exit message
    print("----------- EXITED -----------")

# the get_menu choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print("Friends and Their Birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")
    print()
    
    # get the user's choice.
    choice=int(input("Enter your choice: "))
    # validate the choice.
    while choice<LOOK_UP or choice>QUIT:
        choice=int(input("Enter a valid choice: "))
        
    # return the user's choice.
    return choice

# the look_up function looks up a name in the 
# birthdays dictionary.
def look_up(birthdays):
    # get a name to look up.
    name=input("Enter a name: ")
    
    # look it up in the dictionary.
    print(birthdays.get(name, "Not found."))
    
# the add function adds a new entry into the birtdays dictionary.
def add(birthdays):
    # get a name and birthday.
    name=input("Enter a name: ")
    bday=input("Enter a birthday: ")
    
    # if the name does not exist, add it.
    if name not in birthdays:
        birthdays[name]=bday 
    else:
        print("That entry already exists.")

# the change function changes an existing entry
# in the birthdays dictionary.
def change(birthdays):
    # get a name to look up.
    name=input("Enter a name: ")
    
    if name in birthdays:
        # get a new birthday
        bday=input("Enter the new birthday: ")
        
        # update the entry
        birthdays[name]=bday
    else:
        print("That name is not found.")
        
# the delete function deletes an entry from the 
# birthdays dictionary.
def delete(birthdays):
    # get a name to look up.
    name=input("Enter a name: ")
    
    # if the name is found, delete the entry.
    if name in birthdays:
        del birthdays[name]
    else:
        print("That name is not found.")
        
# call the main function.
main()        
        
    
    