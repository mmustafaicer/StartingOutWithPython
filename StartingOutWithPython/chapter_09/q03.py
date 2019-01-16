# file encryption and decryption

def main():
    # create a dictionary for
    # it is too long copy paste from web
    encrypt={'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
             'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
             'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
             'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
             'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
             't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}
    
    # ask user for encryption or decryption
    print("Welcome to File Encryption and Decryption Program")
    print("1. Encrypt a file.")
    print("2. Decrypt a file.")
    
    choice=int(input("Please enter your choice from above (1 or 2): "))
    print()
    
    if choice==1:
        encryptor(encrypt)
    if choice==2:
        decryptor(encrypt)
        
# first define encryptor function.
def encryptor(encrypt):    
    # open a file to encrypt (read only)
    textfile=open("plaintext.txt", "r")
    
    # read the file's contents and close it
    lines=textfile.readlines()
    textfile.close()
    
    # open a file to write encrypt
    encrypted=open("coded.txt", "w")
    
    # change every character.
    for item in lines:      # this is each item in list.
        for ch in item:     # this is each character in that element
            if ch in encrypt:
                encrypted.write(encrypt[ch])
            else:
                encrypted.write(ch)     # if it is not defined in dict. keep it that way.
                
    print("Your file has been encrypted.")     
    print()       
    # close the file.
    encrypted.close()
    
def decryptor(encrypt):
    # # open a file to decrypt (read only)
    textfile=open("coded.txt", "r")
    
    # read the file's contents and close it
    lines=textfile.readlines()
    textfile.close()
    
    # open a file to write decrypted text
    decrypted=open("uncoded.txt", "w")
    
    # use items method to return each key-value pairs.
    # because we will search for value and get the key for that value.
    listofpairs=encrypt.items()
    
    # change every character.
    for item in lines:      # this is each item in list. (a.k.a each line)
        for ch in item:     # this is each character in that element
            # this time we will search for value and then get the key
            for keyvalue in listofpairs:
                if ch==keyvalue[1]:     # item[1] is value, item[0] is key.
                    decrypted.write(keyvalue[0])    # if ch matched value, print key.
                    found=True                      # set the flag to True.
                    break
                else:
                    found=False
            if not found:
                decrypted.write(ch)     # if it is not defined in dict. (such as . or space just keep it that way)
                    
    print("Your file has been decrypted.")            
    # close the file.
    decrypted.close()
    
# call the main function
main()