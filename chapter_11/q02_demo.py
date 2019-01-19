# ShiftSupervisor Class Demo

import q02
def main():
    
    # get the data from the user.
    print("Please enter the following data.")
    
    emp_name=input("Supervisor Name: ")
    emp_num=int(input("Supervisor Number: "))
    annual_salary=float(input("Please enter annual salary: "))
    annual_bonus=float(input("Please enter your annual bonus: "))
    print()
    
    # create the object
    supervisor=q02.ShiftSupervisor(emp_name, emp_num, annual_salary, annual_bonus)
    
    # display the data
    print("Here is the data that you entered for supervisor.")
    print("---------------------------------------------")
    print("Name:", supervisor.get_employee_name())
    print("Employee Number:", supervisor.get_employee_number())
    print("Annual Salary: $", format(supervisor.get_annual_salary(), ",.2f"), sep="")
    print("Annual Bonus: $", format(supervisor.get_annual_bonus(), ",.2f"), sep="")
    
# call the main function
main()