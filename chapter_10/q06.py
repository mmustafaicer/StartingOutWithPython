# Employee Management System

# this program manages employees data
import pickle
import employee          # this is where our Employee class is.

# global constants for menu choices.
LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

# global constant for the filename.
FILENAME="employees.dat"

# main function
def main():
    # load the existing employees dictionary and
    # assign it to employees.
    employees=load_employees()
    
    # initialize a variable for the user's choice.
    choice=0
    
    # process menu selections until user 
    # wants to quit the program
    while choice!=QUIT:
        # get the user's menu choice.
        choice=get_menu_choice()
        
        # process the choice.
        if choice==LOOK_UP:
            look_up(employees)
        elif choice==ADD:
            add(employees)
        elif choice==CHANGE:
            change(employees)
        elif choice==DELETE:
            delete(employees)
            
    # save the employees dictionary to a file
    save_employees(employees)
    
def load_employees():
    try:
        # open the contacts.dat file.
        input_file=open(FILENAME, "rb")
        
        # unpickle the dictionary.
        employee_dct=pickle.load(input_file)
        
        # close the contacts.dat file
        input_file.close()
        
    except IOError:
        # if could not open the file, so create
        # an empty dictionary.
        employee_dct={}
        
    # return the dictionary.
    return employee_dct

# the get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print("Menu")
    print("-------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee's data.")
    print("4. Delete an employee.")
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
def look_up(employees):
    # get a name to look up.
    id=int(input("Enter ID number: "))
    
    # look it up in the dictionary.
    print()
    print(employees.get(id, "That ID is not found."))       # this is dict's get() function.
    
# the add function adds a new entry into the 
# specified dictionary.
def add(employees):
    # get the contact info.
    id=int(input("Enter a ID Number: "))
    name=input("Name: ")
    dep=input("Department: ")
    job=input("Job: ")
    
    # create a Contact object named entry.
    entry=employee.Employee(id,name,dep, job)
    
    # if the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if id not in employees:
        employees[id]=entry
        print("The entry has been added.")
    else:
        print("That ID already exists.")
        
# the change function changes an existing
# entry in the specified dictionary.

def change(employees):
    # get a name to look up.
    id=int(input("Enter ID number: "))
    
    if id in employees:
        # get a new name
        name=input("Enter the new name: ")
        
        # get a new department.
        dep=input("Enter the new department: ")
        
        # get a new job title.
        job=input("Enter the job title: ")
        
        # create a contact object named entry
        entry=employee.Employee(id,name,dep,job)
        
        # update the entry.
        employees[id]=entry
        print("Information updated.")
    else:
        print("That ID is not found.")
        
# the delete function deletes an entry from the 
# specified dictionary.

def delete(employees):
    # get an ID to look up.
    id=int(input("Enter an ID number: "))
    
    # if the name is found, delete the entry
    if id in employees:
        del employees[id]
        print("Entry deleted!")
    else:
        print("That ID is not found.")
        
# the save_contacts function pickles the specified
# object and saves it to the contacts file.

def save_employees(employees):
    # open the file for writing.
    output_file=open(FILENAME, "wb")
    
    # pickle the dictionary and save it.
    pickle.dump(employees, output_file)
    
    # close the file.
    output_file.close()

# call the main function
main()