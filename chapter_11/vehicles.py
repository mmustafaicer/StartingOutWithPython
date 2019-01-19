# the Automobile class holds general data
# about an automobile in inventory.

class Automobile:
    # the __init__ method accepts arguments for the
    # make, model, mileage, and price. it initializes
    # the data attributes with these values..
    def __init__(self, make, model, mileage, price):
        self.__make=make
        self.__model=model
        self.__mileage=mileage
        self.__price=price
        
    # the following methods are mutators for the
    # class's data attributes.
    def set_make(self, make):
        self.__make=make
        
    def set_model(self, model):
        self.__model=model
        
    def set_mileage(self, mileage):
        self.__mileage=mileage
        
    def set_price(self, price):
        self.__price=price
        
    # the following methods are the accessors
    # for the class's data attributes.
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
    
class Car(Automobile):
    # the __init__ method accepts arguments for the
    # car's make, model, mileage, price, and doors.
    def __init__(self, make, model, mileage, price, doors):
        # call the superclass's __init__ method and pass the
        # required arguments. Note that we also have 
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)    
        
        # initialize the __doors attribute
        self.__doors=doors
        
    # the set_doors method is the mutator for the
    # __doors attribute.
    def set_doors(self, doors):
        self.__doors=doors
        
    # the get_doors method is the accessor for the 
    # __doors attribute
    def get_doors(self):
        return self.__doors
    
# the Truck class represents a pickup truck. It is a
# subclass of the Automobile class.

class Truck(Automobile):
    # the __init__ method accepts arguments for the
    # Truck's make, model, mileage, price, and drive type.
    def __init__(self, make, model, mileage, price, drive_type):
        # call the superclass's __init__ method and pass the
        # required arguments. Note that we also have to pass
        # self as an arugment.
        Automobile.__init__(self, make, model, mileage, price)
        
        # initialize the __drive_type attribute
        self.__drive_type=drive_type
        
    # the set_drive_type method is the mutator for the
    # __drive_type attribute.
    def set_drive_type(self, drive_type):
        self.__drive=drive_type
            
    # the get_drive_type method is the accessor for the
    # __drive_type attribute
    def get_drive_type(self):
        return self.__drive_type
        
# the SUV class represents a sport utility vehicle. it
# is a subclass of the Automobile class.

class SUV(Automobile):
    # the __init__ method accepts arguments for the SUV's mmake,
    # model, mileage, price, and passenger capacity
    def __init__(self, make, model, mileage, price, pass_cap):
        # call the superclass's __init__method and pass the required arguments.
        # note that we also have to pass self as an argument
        Automobile.__init__(self, make, model, mileage, price)
        
        # initialize the __pass_cap attribute.
        self.__pass_cap=pass_cap
        
    # the set_pass_cap method is the mutator for the
    # __pass_cap attribute.
    def set_pass_cap(self, pass_cap):
        self.__pass_cap=pass_cap
        
    # the get_pass_cap method is the accessor for the
    # __pass_cap attribute.
    def get_pass_cap(self):
        return self.__pass_cap
    
    
        
    
    