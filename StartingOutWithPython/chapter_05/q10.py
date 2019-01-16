# feet to inches

def main():
    print("This is a Feet to Inches Converter program.")
    feet=float(input("Enter the feet to be converted: "))
    feet_to_inches(feet)
    
def feet_to_inches(feet):
    inches=feet*12
    print(feet, "feet equals to", inches, "inches.")
    
main()