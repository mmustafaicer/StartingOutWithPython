# Employee Class

class Employee:
    def __init__(self, name, id, dep, job):
        self.__name=name
        self.__id=id
        self.__dep=dep
        self.__job=job 
    
    # mutator methods    
    def set_name(self, name):
        self.__name=name
    
    def set_id(self, id):
        self.__id=id
        
    def set_dep(self, dep):
        self.__dep=dep
        
    def set_job(self, job):
        self.__job=job 
        
    # accessor methods    
    def show_name(self, name):
        return self.__name
    
    def show_id(self, id):
        return self.__id
    
    def show_dep(self, dep):
        return self.__dep
    
    def show_job(self, job):
        return self.__job
    
    # string method for showing
    def __str__(self):
        return "Name: " + self.__name + \
            "\nID Number: " + str(self.__id) + \
            "\nDepartment: " + self.__dep + \
            "\nJob Title: " + self.__job 