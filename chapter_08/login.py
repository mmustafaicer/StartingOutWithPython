# the get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name

def get_login_name(first,last,idnumber):
    
    # get the first three letters of the first name.
    set1=first[0:3]
    
    # get the first three letters of last name.
    set2=last[0:3]
    
    # get the last three characters of the student ID.
    set3=idnumber[-3:]
    
    # put the sets of characters together.
    login_name=set1+set2+set3
    
    # return the login name.
    return login_name

# the valid_password function accepts a password as
# an argument and returns either true or false to indicate
# whether password is valid. A valid password must be at least
# 7 characters in length, have at least one uppercase letter, one 
# lowercase letter and one digit.

def valid_password(password):
    # set the boolean variables to false.
    correct_length=False 
    has_uppercase=False 
    has_lowercase=False 
    has_digit=False 
    
    # begin the validation. start by testing
    # password's length.
    if len(password)>=7:
        correct_length=True 
        
        # test each character and set the appropriate
        # flag when a required character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase=True 
            if ch.islower():
                has_lowercase=True 
            if ch.isdigit():
                has_digit=True 
                
        # determine whether all of the requirements are met.
        # if they are, set is_valid to true.
        # otherwise set is_valid to false.
    if correct_length and has_uppercase and \
    has_lowercase and has_digit:
        is_valid=True 
    else:
        is_valid=False 
        
    # return the is_valid variable.
    return is_valid
                
                
                
                