# Car Class

class Car:
    def __init__(self,year_model, make, speed):
        self.__year_model=year_model
        self.__make=make
        self.__speed=0
        
    def accelerate(self, speed):
        self.__speed+=5
        
    def brake(self, speed):
        self.__speed-=5
        
    def get_speed(self, speed):
        return self.__speed
    
    # write a __str__ method for object's state
    def __str__(self):
        return "The speed is " + str(self.__speed)      # this will be **STRING.**