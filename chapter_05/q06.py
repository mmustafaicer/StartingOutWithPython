# calories from fat and carbohydrates

def main():
    # ask user to enter a gram of fats and carbohydrates
    fats=float(input("Enter the grams of fats you consumed in a day: "))
    carbohydrates=float(input("Enter the grams of carbohydrates you consumed in a day: "))
    fat_calory=caloriesFats(fats)
    carbohydrate_calory=caloriesCarbohydrates(carbohydrates)
    total(fat_calory, carbohydrate_calory)
    
def caloriesFats(fats):
    calory_fat=fats*9
    return calory_fat
def caloriesCarbohydrates(carbohydrates):
    calory_carbohydrates=carbohydrates*4
    return calory_carbohydrates
def total(a,b):
    total_calories=a+b
    print("The calories from fats and carbohydrates are", total_calories, "calories.")
    
main()