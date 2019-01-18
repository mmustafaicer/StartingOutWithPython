# cash register app menu

import q07 

# create your CashRegister object to store retail items
cart=q07.CashRegister()

# prompt user for the description of an item
name=input("Enter the description of the item or q to quit: ")

# keep prompting the user for more items until they're done
while name.lower()!="q":
    # get the rest of the info for the item being purchased
    quantity=int(input("Enter the quantity you'd like to buy: "))
    price_per_unit=float(input("Enter the price for 1 of the item: "))
    price=quantity*price_per_unit
    
    # create a RetailItem object from this info and place in the cart.
    item=q07.RetailItem(name, quantity, price)
    cart.purchase_item(item)
    
    # prompt user for another item or quit
    name=input("Enter the description of the item or 'q' to quit: ")
    
# print out items in the cart as well as total
print()
cart.show_items()
print("Your total: $", cart.get_total(), sep="")