# name and email addresses
import pickle
import os  # for deleting and renaming files.

def main():
    
    # if there is no registry or name_email.dat it will give an error.
    # if there is not file, create a new file, make at least one registry
    # pickle it and close the file. Rerun the program.
    if not os.path.isfile("name_email.dat"):
        # open file for binary writing
        infile = open("name_email.dat", "wb")
        
        # create an empty dictionary.
        emails={}
        
        # ask user to enter one registry
        print("OOPSS! There is no file <<<name_email>>>. Lets create the file and enter one registry.")
        name=input("Enter a name: ").lower()
        emails[name]=input("Enter e-mail address: ")
        
        # pickle the data to file.
        pickle.dump(emails, infile)
        
        # close the file.
        infile.close()
        print("File <<<name_email.dat>>> created.")
        
        # rerun the program.
        main()
    else:
        # read the file for past records
        infile = open("name_email.dat", "rb")
        
        # read the original file and close it
        emails=ReadFile(infile)
        infile.close()
        
        again = "y"  # to control the loop repetition
        # control the loop if the user wants to again
        while again.lower() == "y":
            print()
            print("MENU")
            print("1: Add a new name and email address")
            print("2: Change an existing email address")
            print("3: Delete an existing email address")
            print("4: Show data for")
            print("------------------------------------")
            
            # set a flag if user has made changes or just view data
            # if did not change, there is no need to write the file.
            status=False
            
            # ask user for input
            user_choice = int(input("Please enter a choice among the menu (1,2,3,4): "))
            if user_choice == 1:
                new_dict = AddNewName(emails)
                status=True
            elif user_choice == 2:
                new_dict = Change(emails)
                status=True
            elif user_choice == 3:
                new_dict = Delete(emails)
                status=True
            elif user_choice == 4:
                ShowDataFor(emails)
            else:
                print("You entered an invalid option.")
            print()
            again = input("You want to continue? (y or n): ")
            print()

        # after user done we will save and close
        # pickle it to the file.
        # open a new file for writing..
        newfile = open("temp.dat", "wb")
        if status:                      # if changes has made, then write it. otherwise dont.
            pickle.dump(new_dict, newfile)
            newfile.close()
            # delete the original file.
            os.remove("name_email.dat")

            # rename the new file.
            os.rename("temp.dat", "name_email.dat")
            
            print("The file has been saved.")
        infile.close()
        print("EXITED")

def ReadFile(infile):
    end_of_file = False  # to indicate the end of file
    while not end_of_file:
        try:
            # unpickle the next object
            store = pickle.load(infile)
            
        except EOFError:
            # set the flag to indicate the end
            end_of_file = True
    return store    
def AddNewName(emails):
    # get the data and save it
    name = input("Please enter the name: ")
    if name.lower() not in emails:
        emails[name.lower()] = input("E-mail: ")
        print("The registry for", name, "has been recorded.")
    else:
        print("That name already exists.")
    return emails

def Change(emails):
    # ask user for the change.
    name = input("What is the name you want to change email address: : ")
    if name.lower() in emails:
        emails[name.lower()] = input("Enter new e-mail: ")
        print("The registry for", name, "has been updated.")
    else:
        print("It is not found in the file.")
    return emails

def Delete(emails):
    # ask user for the deletion.
    name = input("What is the name you want to remove email address for: ")
    if name.lower() in emails:
        del emails[name.lower()]
        print("The registry for", name, "has been deleted.")
    else:
        print("It is not found in the file.")
    return emails

def ShowDataFor(emails):
    try:
        name = input("What is the name you are looking for?: ")
        print("Email address: ", emails[name.lower()])
    except KeyError:
        print("The key", name, "is not found.")
        print()

# call the main function
main()