# this program demonstrates the Car class.

import vehicles

def main():
    # create an object from the Car class.
    # the car is 2007 Audi with 12,500 miles, priced
    # at $21,500.00 and has 4 doors.
    used_car=vehicles.Car("Audi", 2007, 12500, 21500.00, 4)
    
    # display the car's data.
    print("Make:", used_car.get_make())
    print("Model:", used_car.get_model())
    print("Mileage:", used_car.get_mileage())
    print("Price:", used_car.get_price())
    print("Number of doors:", used_car.get_doors())
    
# call the main function
main()