# test average and grade

def main():
    # ask user to enter test scores
    test1=int(input("Enter the grade for test 1: "))
    test2=int(input("Enter the grade for test 2: "))
    test3=int(input("Enter the grade for test 3: "))
    test4=int(input("Enter the grade for test 4: "))
    test5=int(input("Enter the grade for test 5: "))
    print()
    print("Score\t\tLetter Grade")
    print("-------------------------")
    determine_grade(test1, test2, test3, test4, test5)
    print()
    average=calc_average(test1,test2,test3,test4,test5)
    print("Your average is", format(average, ",.2f"))
    
def calc_average(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    return average

def determine_grade(a,b,c,d,e):
    for grade in (a,b,c,d,e):
        if grade>=90 and grade<=100:
            print(grade, "\t\t", "A")
        elif grade>=80 and grade<=89:
            print(grade, "\t\t", "B")
        elif grade>=70 and grade<=79:
            print(grade, "\t\t", "C")
        elif grade>=60 and grade<=69:
            print(grade, "\t\t", "D")
        elif grade>=0 and grade<60:
            print(grade, "\t\t", "F")
        else:
            print("Error! You entered an invalid test score!")
            
main()
            