# name search

def main():
    
    # read the files. files are in the repository
    boy_names=open("BoyNames.txt", "r")
    girl_names=open("GirlNames.txt", "r")
    
    # read then into list without "\n"
    # use splitlines method. check documentation
    boy_list=boy_names.read().splitlines()
    girl_list=girl_names.read().splitlines()
    
    # get the names from user.
    user_boy=input("Enter a boy's name (first letter capital): ")
    user_girl=input("Enter a girl's name (first letter capital): ")
    print()
    
    # check names if they are in the list
    CheckNames(boy_list, girl_list, user_boy,user_girl)
    
def CheckNames(boy_list, girl_list, user_boy,user_girl):
    
    # search for boy name
    if user_boy in boy_list:
        print("The boy name <<", user_boy, ">> is in the list.", sep="")
    else:
        print("The boy name <<", user_boy, ">> is NOT in the list.", sep="")
    
    # search for girl name    
    if user_girl in girl_list:
        print("The girl name <<", user_girl, ">> is in the list.", sep="")
    else:
        print("The girl name <<", user_girl, ">> is NOT in the list.", sep="")    

# call the main function
main()