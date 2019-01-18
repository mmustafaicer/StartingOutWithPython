# Employee Class (Alternative)

import q04 

def main():
    emp_list=[]
    
    # create a list for employee data
    names=["Susan Meyers", "Mark Jones", "Joy Rogers"]
    idnums=["47899", "39119", "81774"]
    depart=["Accounting", "IT", "Manufacturing"]
    job_title=["Vice President", "Programmer", "Engineer"]
    
    # get the data and add it to object
    for i in range(0,3,1):
        name=names[i]
        id=idnums[i]
        dep=depart[i]
        job=job_title[i]
        
        # add it to object.
        employee=q04.Employee(name, id, dep, job)
        emp_list.append(employee)
        
    # show the data.
    for item in emp_list:
        print(item)
        print()
        
# call the main function
main()