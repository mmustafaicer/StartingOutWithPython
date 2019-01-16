# this program reads a file's contents into a list.

def main():
    # open a file for reading.
    infile=open("cities.txt", "r")
    
    # read the contents of the file into a list.
    cities=infile.readlines()
    
    # close the file
    infile.close()
    
    # strip the \n from each element.
    index=0
    while index<len(cities):
        cities[index]=cities[index].rstrip("\n")
        index+=1
    
    # print the contents of the list.
    print(cities)
    
# call the main function.
main()