# personal Information class

import q03

def main():
    # create an empty list for storing objects.
    info=[]
    
    # get the data from the user.
    print("Enter the information for 3. One is for you. Other two for friends.")
    for i in range(3):
        name=input("Name: ")
        address=input("Address: ")
        age=int(input("Age: "))
        phone_number=int(input("Phone number: "))
        print()
        
        # create an object.
        person=q03.Information(name, address, age, phone_number)
        
        # add the object to the list
        info.append(person)
        
    print("The data has been saved.")
    
    # display the data.
    print()
    print("Here is the information you entered.")
    
    # item refers to an object in each iteration. 1st instance, 
    # 2nd instance, and 3rd instance.
    for item in info:
        print("Name: ", item.show_name())
        print("Address: ", item.show_address())
        print("Age: ", item.show_age())
        print("Phone Number: ", item.show_phone_number())
        print()
    
# call the main function
main()
    