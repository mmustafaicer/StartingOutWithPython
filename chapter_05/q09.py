# monthly sales tax

# write constants
STATE_TAX_RATE=0.05
COUNTY_TAX_RATE=0.025

def main():
    # ask user to enter the total sales for the month
    total_sales=float(input("Enter the total sales for the month: "))
    print()
    c_tax_total=CountyTaxCalculator(total_sales)
    s_tax_total=StateTaxCalculator(total_sales)
    TotalTaxCalculator(c_tax_total,s_tax_total)
    
def CountyTaxCalculator(total_sales):
    county_tax=total_sales*COUNTY_TAX_RATE
    print("Your county sales tax is $", format(county_tax, ",.2f"), sep='')
    return county_tax
def StateTaxCalculator(total_sales):
    state_tax=total_sales*STATE_TAX_RATE
    print("Your state sales tax is $", format(state_tax, ",.2f"), sep='')
    return state_tax
def TotalTaxCalculator(a,b):
    total=a+b
    print("Your total sales tax is $", format(total, ",.2f"), sep='')
    
main()