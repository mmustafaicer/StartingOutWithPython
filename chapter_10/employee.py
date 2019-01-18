# Employee Class

class Employee:
    def __init__(self, id, name, dep, job):  # since id will be key. first argument will be id
        self.__id=id
        self.__name=name
        self.__dep=dep
        self.__job=job 
    
    # mutator methods    
    def set_id(self, id):
        self.__id=id
    
    def set_name(self, name):
        self.__name=name
    
    def set_dep(self, dep):
        self.__dep=dep
        
    def set_job(self, job):
        self.__job=job 
        
    # accessor methods    
    def show_id(self, id):
        return self.__id
    
    def show_name(self, name):
        return self.__name
    
    def show_dep(self, dep):
        return self.__dep
    
    def show_job(self, job):
        return self.__job
    
    # string method for showing
    def __str__(self):
        return "ID Number: " + str(self.__id) + \
            "\nName: " + self.__name + \
            "\nDepartment: " + self.__dep + \
            "\nJob Title: " + self.__job 