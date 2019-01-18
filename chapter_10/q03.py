# personal Information class

class Information:
    def __init__(self, name, address, age, phone_number):
        self.__name=name
        self.__address=address
        self.__age=age
        self.__phone_number=phone_number
    
    # mutator methods    
    def set_name(self, name):
        self.__name=name
        
    def set_address(self, address):
        self.__address=address
        
    def set_age(self, age):
        self.__age=age
        
    def set_phone_number(self, phone_number):
        self.__phone_number=phone_number
        
    # accessor methods
    def show_name(self):
        return self.__name
    
    def show_address(self):
        return self.__address
    
    def show_age(self):
        return self.__age
    
    def show_phone_number(self):
        return self.__phone_number
    
    # create a method for showing object's state
    def __str__(self):
        return "Name: " + (self.__name) +\
            "\nAddress: " + str(self.__address) +\
            "\nAge: " + str(self.__age) +\
            "\nPhone Number: " + str(self.__phone_number)