# Car class

class Car:
    def __init__(self, make, model, year):
        self.__make=make
        self.__model=model 
        self.__year=year
        
    def set_make(self, make):
        self.__make=make 
        
    def set_model(self, model):
        self.__model=model 
        
    def set_year(self, year):
        self.__year=year
        
    def get_make(self, make):
        return self.__make
    
    def get_model(self, model):
        return self.__model
    
    def get_year(self, year):
        return self.__year
    