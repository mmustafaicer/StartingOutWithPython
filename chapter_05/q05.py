# property tax

# set constants
ASSESSMENT_RATE=0.60

def main():
    property_value=float(input("Please enter the property's actual value: "))
    assessment_amount=assessment_value(property_value)
    tax_value=calculate_tax(assessment_amount)
    
def assessment_value(property_value):
    assess_value=property_value*ASSESSMENT_RATE
    print("Your property's assessment value is $", format(assess_value, ",.2f"))
    return assess_value
    
def calculate_tax(assessment_amount):
    total_property_tax=assessment_amount*0.0072          # 72 cents for each $100. 
    print("Your total tax is $", format(total_property_tax, ",.2f"))
    return total_property_tax

# call the main function
main()
    