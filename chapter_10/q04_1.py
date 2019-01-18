# Employee Class

# there is an alternative to this.
import q04 

def main():
    # create a list for employee data
    emp_list=[]
    
    # get the data and add it to object
    for i in range(3):
        name=input("Name: ")
        id=int(input("ID Number: "))
        dep=input("Department: ")
        job=input("Job Title: ")
        print()
        
        # add it to object.
        employee=q04.Employee(name, id, dep, job)
        emp_list.append(employee)
        
    # show the data.
    for item in emp_list:
        print(item)
        print()
        
# call the main function
main()