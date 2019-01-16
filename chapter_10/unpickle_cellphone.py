# this program unpickles CellPhone objects.
import pickle
import cellphone 

# constant for the filename.
FILENAME="cellphones.dat"

def main():
    end_of_file=False       # to indicate the end of file
    
    # open the file.
    input_file=open(FILENAME, "rb")
    
    # read to the end of file.
    while not end_of_file:
        try:
            # unpickle the next object.
            phone=pickle.load(input_file)
            
            # display the cell phone data.
            display_data(phone)
        except EOFError:
            # set the flag to indicate the end
            # of the file has been reached.
            end_of_file=True 
            
    # close the file.
    input_file.close()
    
# the display_data function displays the data
# from the CellPhone object passed as an argument.
def display_data(phone):
    print("Manufacturer: ", phone.get_manufact())
    print("Model Number: ", phone.get_model())
    print("Retail price: $", format(phone.get_retail_price(), ",.2f"), sep="")
    print()
    
# call the main function.
main()