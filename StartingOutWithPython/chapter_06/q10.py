# golf scores

def main():
    try:
        # ask user how many members' data will be entered
        num_members=int(input("Enter the number of members for data entry: "))
        write(num_members)
        read()
    except ValueError:
        print("ERROR: Please enter a positive integer for number of members.")
        main()
    
def write(num_members):
    
    # open a file for writing
    golf_file=open("golf.txt", "w")
    
    # ask user for member name and score
    for i in range(1,num_members+1,1):
        # get the input
        print("Please enter the name of Member #", i, end="")
        member_name=input(": ")
        print("Please enter the score for Member #", i, end="")
        member_score=input(": ")
        
        # write it to the files.
        golf_file.write(member_name + "\n")
        golf_file.write(member_score + "\n")
    
    print()    
    print("Your entries have been recorded to <golf.txt> file.")
    print()
    
    # close the file.
    golf_file.close()
    
def read():
    
    # open file for reading
    golf_file=open("golf.txt", "r")
    
    # read the first line
    name=golf_file.readline()
    print("Member Name\t\tScore")
    print("-------------------------------")
    
    # read the rest of the file
    while name!="":
        # read the rest of the line.
        score=golf_file.readline()
        
        # strip \n s from the file.
        name=name.rstrip("\n")
        score=score.rstrip("\n")
        print(name, "\t\t", score)
        
        name=golf_file.readline()
        
    # close the file after reading
    golf_file.close()
    
# call the main function
main()
    
    