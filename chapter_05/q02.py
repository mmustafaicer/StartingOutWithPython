# sales tax program refactoring

def main():
    global purchase
    purchase=float(input("Enter the amount of purchase: "))
    print()
    print("Your purchase amount is $", purchase, sep='')
    s_tax=state_tax(purchase)
    c_tax=county_tax(purchase)
    t_tax=total_tax(s_tax,c_tax)
    print()
    total(purchase, t_tax)

# write subtasks in functions
def state_tax(sales):
    s_tax=sales*0.05
    print("Your state tax is $", format(s_tax, ".2f"), sep='')
    return s_tax
def county_tax(sales):
    c_tax=sales*0.025
    print("Your county tax is $", format(c_tax, ".2f"), sep='')
    return c_tax
def total_tax(s_tax, c_tax):
    t_tax=s_tax+c_tax
    print("Your total tax is $", t_tax, sep='')
    return t_tax
def total(purchase, t_tax): 
    total=purchase+t_tax
    print("Your total is $", format(total, ",.2f"))
    
# call main function
main()