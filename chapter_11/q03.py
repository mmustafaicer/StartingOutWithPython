# Person and Customer classes

class Person:
    def __init__(self, name, address, phone_num):
        self.__name=name
        self.__address=address
        self.__phone_num=phone_num
        
    # set accessor methods.
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone_num(self):
        return self.__phone_num
    
# customer is a subclass of Person superclass
class Customer(Person):
    def __init__(self, name, address, phone_num, cust_num, mail_list):
        
        # pass superclass' __init__ method.
        Person.__init__(self, name, address, phone_num)
        
        # initialize the data attributes of subclass
        self.__cust_num=cust_num
        self.__mail_list=mail_list
        
        # set accessor
    def get_cust_num(self):
        return self.__cust_num
    
    def get_mail_list(self):
        if self.__mail_list==1:
            status=True     # to keep status of mailing list
            return "Yes"
        else: 
            status=False 
            return "No"