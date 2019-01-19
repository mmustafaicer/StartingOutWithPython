# ShiftSupervisor Class

# Employee class from q01
class Employee:
    # the __init__ method initializes the data attributes
    # for the employee name and employee number
    def __init__(self, emp_name, emp_num):
        self.__employee_name=emp_name
        self.__emplyee_number=emp_num
        
    # the following are mutator methods for class's
    # data attributes
    def set_employee_name(self, emp_name):
        self.__employee_name=emp_name
        
    def set_employee_number(self, emp_num):
        self.__emplyee_number=emp_num
        
    # the following are accessor methods for class's
    # data attributes
    def get_employee_name(self):
        return self.__employee_name
    
    def get_employee_number(self):
        return self.__emplyee_number
    
# ShiftSupervisor is a subclass of Employee class

class ShiftSupervisor(Employee):
    # __init__ method should have all data attributes.
    def __init__(self, emp_name, emp_num, annual_salary, annual_bonus):
        # pass the superclass' __init__ method
        Employee.__init__(self, emp_name, emp_num)
        
        # initialize the data attributes of subclass
        self.__annual_salary=annual_salary
        self.__annual_bonus=annual_bonus
        
    # create accessor methods for new data attributes.
    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus
    
    
    