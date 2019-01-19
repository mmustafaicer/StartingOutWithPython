# Employee and ProductionWorker classes demo

import q01

def main():
    # get the data from user
    print("Please enter the following data.")
    
    emp_name=input("Employee Name: ")
    emp_num=int(input("Employee Number: "))
    shift_num=int(input("Shift Number (1 for day 2 for night): "))    
    pay_rate=float(input("Enter hourly pay rate: "))
    print()
    
    # create an object of ProductionWorker.
    employee=q01.ProductionWorker(emp_name, emp_num, shift_num, pay_rate)

    # display the data
    print("Here is the data that you entered.")
    print("------------------------------------")
    print("Name:", employee.get_employee_name())
    print("Employee Number:", employee.get_employee_number())
    print("Shift time:", employee.get_shift_number())
    print("Hourly pay rate: $", format(employee.get_pay_rate(), ",.2f"), sep="")
    
# call the main function
main()