# RetailItem Class

class RetailItem:
    def __init__(self, descr, units, price):
        self.__descr=descr
        self.__units=units
        self.__price=price
        
    # mutator methods
    def set_descr(self, descr):
        self.__descr=descr
        
    def set_units(self, units):
        self.__units
        
    def set_price(self, price):
        self.__price 
        
    # accessor methods
    def show_descr(self):
        return self.__descr
    
    def show_units(self):
        return self.__units 
    
    def show_price(self):
        return self.__price 
    
    # set string method
    
    def __str__(self):
        return "Description: " + self.__descr+ \
            "\nUnits in Inventory: " + str(self.__units) + \
            "\nPrice: $" + str(self.__price)