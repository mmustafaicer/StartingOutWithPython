# how much insurance

def main():
    cost_house=float(input("Enter the replacement cost of a building: "))
    print()
    insurance(cost_house)
    
# write insurance function
def insurance(cost_house):
    insurance_amount=cost_house*0.80
    print("Your insurance amount is $", format(insurance_amount, ",.2f"))
    
# call the main function
main()