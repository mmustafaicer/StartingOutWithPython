# this program gets the user's first name, last name, and
# student ID number. Using this data it generates a system 
# login name.

import login

def main():
    # get the user's first name, last name, and ID number
    first=input("Enter your first name: ")
    last=input("Enter your last name: ")
    idnumber=input("Enter your student ID number: ")
    
    # get the login name.
    print("Your system login name is:")
    print(login.get_login_name(first,last,idnumber))
    
# call the main function
main()