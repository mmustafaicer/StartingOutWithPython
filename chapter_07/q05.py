# charge account validation

def main():
    file_numbers=ReadFile()
    user_number=GetUserNumber()
    print()
    status=CheckFile(file_numbers, user_number)
       
def ReadFile():
    # open file for reading
    myfile=open("charge_accounts.txt", "r")
    
    # read the lines in the file.
    file_numbers=(myfile.readlines())
    
    # strip the \n from each element. Also convert into integer.
    index=0
    while index<len(file_numbers):
        file_numbers[index]=int(file_numbers[index].rstrip("\n"))
        index+=1
    
    # return the list.
    return file_numbers

def GetUserNumber():
    # get the number from user
    print("Please enter the charge account number", end="")
    user_number=int(input(": "))
    
    # return user number
    return user_number

def CheckFile(a,b):
    if b in a:
        print("The number",b,"is valid. It is in the file.")
    else:
        print("***ERROR***:The number", b,"is NOT valid. It is not found in the file.")
# call the main function
main()