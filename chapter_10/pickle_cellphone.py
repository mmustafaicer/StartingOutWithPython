# this program pickles CellPhone objects.
import pickle 
import cellphone

# constant for the file name.
FILENAME="cellphones.dat"

def main():
    # initialize a variable to control the loop.
    again="y"
    
    # open a file.
    output_file=open(FILENAME, "wb")
    
    # get the data from the user.
    while again.lower()=="y":
        # get the cell phone data.
        man=input("Enter the manufacturer: ")
        mod=input("Enter the model number: ")
        retail=float(input("Enter the retail price: "))
        
        # create a CellPhone object.
        phone=cellphone.CellPhone(man,mod,retail)
        
        # pickle the object and write it to the file.
        pickle.dump(phone, output_file)
        
        # get more cell phone data?
        again=input("enter more phone data? (y/n): ")
        
    # close the file.
    output_file.close()
    print("The data was written to", FILENAME)

# call the main function
main()