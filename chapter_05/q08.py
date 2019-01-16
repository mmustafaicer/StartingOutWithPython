# paint job estimator

# write constants (global variables)
                 
PAINT_PER_FOOT=1/112            # gallon of paint for 1 square foot
LABOR_PER_FOOT=8/112            # required hour of labor for 1 square foot
CHARGE_FOR_HOUR=35              # $35 for 1 labor hour

def main():
    # ask user to enter the square feet of wall space
    wall_space=float(input("Enter the square feet of wall to be painted: "))
    price_paint=float(input("Enter the price of the paint per gallon: "))
    print()
    num_gal=numberOfGallons(wall_space)
    num_hour=numberOfHours(wall_space)
    cost_paint=costOfPaint(num_gal, price_paint)
    cost_labor=LaborCharges(num_hour)
    total_cost=TotalOfCharges(cost_paint, cost_labor)
    
def numberOfGallons(wall_space):
    number_of_gallons=wall_space*PAINT_PER_FOOT
    print("You will need",number_of_gallons, "gallons of paint.")
    return number_of_gallons
def numberOfHours(wall_space):
    number_of_hours=wall_space*LABOR_PER_FOOT
    print("You will need", number_of_hours, "hours of labor.")
    return number_of_hours
def costOfPaint(num_gal, price_paint):
    cost_of_paint=num_gal*price_paint
    print("The cost of paint is $", format(cost_of_paint, ",.2f"), sep='')
    return cost_of_paint
def LaborCharges(num_hour):
    cost_of_labor=num_hour*CHARGE_FOR_HOUR
    print("The cost of labor is $", format(cost_of_labor, ",.2f"), sep='')
    return cost_of_labor
def TotalOfCharges(cost_paint, cost_labor):
    total_charges=cost_paint+cost_labor
    print("Your total charges are $", format(total_charges, ",.2f"), sep='')

main()
    
    
    