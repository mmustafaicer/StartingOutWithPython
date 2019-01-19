# Person and Customer Class demo

import q03

def main():
    # get the data from the user.
    print("Please enter the following data.")
    name=input("Name: ")
    address=input("Address: ")
    phone_num=input("Phone number: ")
    cust_num=int(input("Customer number: "))
    mail_list=int(input("Do you want to be in our mailing list? (0=no 1=yes): "))
    
    # create the object with these data attributes
    customer=q03.Customer(name, address, phone_num, cust_num, mail_list)
    
    # display the data.
    print()
    print("Here is the data you entered.")
    print("------------------------------")
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Phone number:", customer.get_phone_num())
    print("Customer number:", customer.get_cust_num())
    print("Mailing List:", customer.get_mail_list())
    
# call the main function
main()