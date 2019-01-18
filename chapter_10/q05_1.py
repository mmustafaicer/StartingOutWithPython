# RetailItem Class

import q05
def main():
    # create an empty item list
    items_list=[]
    
    
    descr_list=["Jacket", "Designer Jeans", "Shirt"]
    units_list=[12, 40, 20]
    price_list=[59.95, 34.95, 24.95]
    
    # create three objects from RetailItem Class
    for i in range(0,3,1):
        descr=descr_list[i]
        units=units_list[i]
        price=price_list[i]
        
        # create each instance
        item=q05.RetailItem(descr, units, price)
        
        # write it to the list.
        items_list.append(item)
        
    # print the data
    for item in items_list:
        print(item)
        print()
        
# call the main function
main()