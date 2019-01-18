# import Car class from q02.py

import q02

def main():
    
    # create an Car class object.
    year_model=input("Please enter your car's year and model (example: 2008 Altima): ")
    make=input("Please enter your car's make (example: Nissan): ")
    speed=0         # even though we make this lets say 50. It will be zero. Because it is privately
    print()         # defined in Car class. __speed=0 << remember.
    
    # create a Car object
    mycar=q02.Car(year_model,make,speed)
    
    # create a loop to call accelerate method 5 times.
    for i in range(5):
        mycar.accelerate(speed)
        print(mycar)            # this will call for __str__ method.
        
    # create a loop to call brake method five times.
    print()
    for i in range(5):
        mycar.brake(speed)
        print(mycar)            # this will call for __str__ method.
        
# call the main function.
main()