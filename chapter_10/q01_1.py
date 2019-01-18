# import the Pet the class stored in q01 module

import q01

def main():
    # get the data from the user.
    name=input("Enter a animal name: ")
    animal_type=input("Enter the animal type: ")
    age=int(input("Enter the age: "))
    
    # create the object.
    my_animal=q01.Pet(name, animal_type, age)
    
    # display the data
    print()
    print("Name: ", my_animal.get_name(name))
    print("Animal Type: ", my_animal.get_animal_type(animal_type))
    print("Age: ", my_animal.get_age(age))
    
# call the main function
main()
    
    