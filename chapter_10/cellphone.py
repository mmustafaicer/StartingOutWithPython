# The CellPhone ckass holds data about a cell phone.

class CellPhone:
    # the __init__ method initializes the attributes.
    def __init__(self, manufact, model, price):
        self.__manufact=manufact
        self.__model=model
        self.__retail_price=price
        
    # the set_manufact method accepts an argument for
    # the phone's manufacturer.
    def set_manufact(self, manufact):
        self.__manufact=manufact
        
    # the set_model method accepts an argument for
    # the phone's model number.
    def set_model(self, model):
        self.__model=model 
        
    # the set_retail_price method accepts an argument
    # for the phone's retail price.
    def set_retail_price(self, price):
        self.__retail_price=price 
        
    # the get_manufact method returns the
    # phone's manufacturer.
    def get_manufact(self):
        return self.__manufact
    
    # the get_model method returns the
    # phone's model number.
    def get_model(self):
        return self.__model
    
    # the get_retail_price method returns the
    # phone's retail price.
    def get_retail_price(self):
        return self.__retail_price