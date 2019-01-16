# software sales

# ask user to enter number of packages that he or she will purchase
n_purchase=int(input("Enter the number of packages you would like to buy: "))
# each pack cost $99
package_unit_cost=99

print()

# create decision structure for given discounts.
if n_purchase>0 and n_purchase<10:
    subtotal=n_purchase*package_unit_cost
    disc_rate=0
    discounted_amount=n_purchase*package_unit_cost*disc_rate
    total=(n_purchase*package_unit_cost)-discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif n_purchase>=10 and n_purchase<=19:
    subtotal=n_purchase*package_unit_cost
    disc_rate=0.10
    discounted_amount=n_purchase*package_unit_cost*disc_rate
    total=(n_purchase*package_unit_cost)-discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif n_purchase>=20 and n_purchase<=49:
    subtotal=n_purchase*package_unit_cost
    disc_rate=0.20
    discounted_amount=n_purchase*package_unit_cost*disc_rate
    total=(n_purchase*package_unit_cost)-discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif n_purchase>=50 and n_purchase<=99:
    subtotal=n_purchase*package_unit_cost
    disc_rate=0.30
    discounted_amount=n_purchase*package_unit_cost*disc_rate
    total=(n_purchase*package_unit_cost)-discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif n_purchase>=100:
    subtotal=n_purchase*package_unit_cost
    disc_rate=0.40
    discounted_amount=n_purchase*package_unit_cost*disc_rate
    total=(n_purchase*package_unit_cost)-discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
else:
    print("ERROR: You entered an invalid response.")
    