# automobile costs

def main():
    loan=loan_payment()
    insurance=insurance_cost()
    gas=gas_cost()
    oil=oil_cost()
    tires=tires_cost()
    maintenance=maintenance_cost()
    total_expenses=total_cost(loan, insurance, gas, oil, tires, maintenance)
    
    print("Your monthly total cost is $", total_expenses)
    
# write a function for each subtask
def loan_payment():
    loan=float(input("Please enter the cost of loan: "))
    return loan
def insurance_cost():
    insurance=float(input("Please enter the cost of insurance: "))
    return insurance
def gas_cost():
    gas=float(input("Please enter the cost of gas: "))
    return gas
def oil_cost():
    oil=float(input("Please enter the cost of oil: "))
    return oil
def tires_cost():
    tires=float(input("Please enter the cost of tires: "))
    return tires
def maintenance_cost():
    maintenance=float(input("Please enter the cost of maintenance: "))
    return maintenance
def total_cost(loan, insurance, gas, oil, tires, maintenance):
    total=loan+insurance+gas+oil+tires+maintenance
    return total

# call the main function
main()
    