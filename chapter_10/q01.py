# Pet Class

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
        
    def set_name(self, name):
        self.__name=name
        
    def set_animal_type(self, animal_type):
        self.__animal_type=animal_type
    
    def set_age(self, age):
        self.__age=age
        
    def get_name(self, name):
        return self.__name
    
    def get_animal_type(self, animal_type):
        return self.__animal_type
    
    def get_age(self, age):
        return self.__age
    
    