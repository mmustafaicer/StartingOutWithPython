# alphabetic telephone number translator

def main():
    # create two lists for conversion. each index will match in two lists.
    # for example. a=2, b=2, c=2
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y''z']
    number =[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
    
    # get the input from the user.
    phone = input('Enter a phone number in the format xxx-xxx-xxxx: ') # or you can add end .lower() to lowercase.
    
    # convert to lower case.
    phone=phone.lower() 
    
    # go through each character in input
    index = 0
    while index<len(phone):

        # if it is alphabetical convert it, if it is not (4,5, or -) keep it.
        if phone[index].isalpha():
            print(number[alpha.index(phone[index])], end="")
        else:
            print (phone[index], end = "")
        index+=1

main()
