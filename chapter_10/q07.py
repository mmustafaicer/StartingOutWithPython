# cash register
# for clarity, i will do both classes in this file.

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



# CashRegister Class
# got help from slader.com
            
class CashRegister:
    def __init__(self):
        # initialize the CashRegister object with an empty list called cart.
        # this is where RetailItems to be purchased will be stored.
        self.__cart=[]
    
    # add purchased item to the cart. This is made a bit more complicated
    # because I want to be able to add the same item more than once without
    # it appearing as separate items in the list.    
    def purchase_item(self, item):
        # create a list of all descriptions of the items already in the cart.
        cart_descriptions=[]
        for retail_item in self.__cart:
            cart_descriptions.append(retail_item.show_descr())
        
        # if the purchased item isn't already in the cart, then just add it in
        if item.show_descr() not in cart_descriptions:
            self.__cart.append(item)
            
        # otherwise we have to find it in the cart and update the quantity and price
        else:
            for i in range(len(self.__cart)):
                if item.show_descr()==self.__cart[i].show_descr():
                    self.__cart[i].set_units(self.__cart[i].show_units()+item.show_units())
                    self.__cart[i].set_price(self.__cart[i].show_price()+ item.show_price())
    
    # calculate and return the total cost of all items in the cart.                
    def get_total(self):
        total=0
        for item in self.__cart:
            total+=item.show_price()
            return format(total, ",.2f")
    
    # display a list of all items in the cart with their quantity and price            
    def show_items(self):
        print("Your cart")
        for item in self.__cart:
            print(item)
            print("---------------")        
    
    # clear the contents of the cart
    def clear(self):
        # clear the shopping cart.
        self.__cart=[]
        
        