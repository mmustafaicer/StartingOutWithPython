# this program creates a Car object, a Truck object,
# and an SUV object.

import vehicles

def main():
    # create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    car=vehicles.Car("BMW", 2001, 70000, 15000.0, 4)
    
    # create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4 wheel drive.
    truck=vehicles.Truck("Toyota", 2002, 40000, 12000.0, "4WD")
    
    # create an SUV object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    suv=vehicles.SUV("Volvo", 2000, 30000, 18500.0, 5)
    
    print("USED CAR INVENTORY")
    print("===================")
    
    # display the car's data
    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Number of doors:', car.get_doors())
    print()
    
    # display the truck's data.
    print("The following pickup truck is in inventory.")
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())
    print()
    
    # display the SUV's data.
    print("The following SUV is in inventory.")
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())

# call the main function
main()
