from DBS import *
from time import sleep

# user sign-in details 
SIGNINUSER = None

# main menu 
def mainMenu():
    print("""
--------------------    
Welcome To Passvault

    ---menu---

1-> Create User
2-> Login User
0-> Exit   
    ----------""" )


# User dash board
def intomenu(user):
    print(f"""
    ---------
Welcome {user}""")
    print("""

    ---MENU---
1-> View a password
2-> Add a new password
3-> View all passwords
0-> Exit  
    ---------- """  )

# New user creater
def createNewUser():
    global SIGNINUSER
    print('-'*25)
    username = input("Enter a username :")
    check = True
    while check:
        if checkAvaliableUsername(username):
            check = False
        else:
            username  = input("Username is already taken! Try another user name:")    

    password = input("Enter a master password :")
    confirm = input("Confirm password :")
    while password !=  confirm:
        print("Password does not match !!")
        password = input("Enter a master password :")
        confirm = input("Confirm password :")
    else:
        SIGNINUSER = createUser(username,password)   
    return True

# sign in an existing user
def signUser():
    print('-'*25)
    username =  input("Username: ")
    password = input("Password: ")
    global SIGNINUSER 
    SIGNINUSER = signInUser(username,password)
    if  not SIGNINUSER:
        print("Invalid Credentials")
        return False
    return True


# View password for a specific site    
def viewPassword():
    print('-'*25)
    siteName = input('Sitename :')
    passwords = passwordFinder(siteName,SIGNINUSER)
    if len(passwords) == 0:
        print('-'*25)
        print(f"No passwords for the {siteName} is safed in ur database!")
        print('-'*25)
        return
    else:
        print("Found Passwords :")
        print('-'*25)
        for row in passwords:
            print(f'SiteName : {row[0]}')
            print(f'Url : {row[1]}')
            print(f'Password : {row[2]}')
            print('-'*25)
    x = input('Press a Key to  Return')
    if x != None:
        return        

# add a new password site set
def addNewpassword():
    print('-'*25)
    print("Add a new password")
    sitename = input("Enter site name :")
    url = input("Enter site url :")
    password = input("Enter password :")
    createPassword(sitename,url,password,SIGNINUSER)
    print(f"Password for {sitename} saved!")

# View all password saved in for a user
def allpasword():
    passwords = fitchAllPassword(SIGNINUSER)
    if len(passwords) == 0:
        print('-'*25)
        print("You don't have any password saved Yet!")
        print('-'*25)
        return
    print('-'*25)
    for row in passwords:
            print(f'SiteName : {row[0]}')
            print(f'Url : {row[1]}')
            print(f'Password : {row[2]}')
            print('-'*25)
    x = input('Press a key to  Return')
    if x != None:
        print('-'*25)
        return        

# MAIN DRIVER FUNCTION
def main():

    # create db
    createdb()

    # a sudo choice 
    choice = 9

    while choice != 0:
        if SIGNINUSER == None:
            mainMenu()
            try:
                choice = int(input("Enter an option :"))
            except:
                print("Invalid Input")
                continue    
            if choice == 1:
                createNewUser()
            elif choice == 2:
                signUser()        
        else:
            intomenu(SIGNINUSER[1])
            try:
                choice = int(input())
            except:
                print("Invalid Input")
                continue    
            if choice == 1:
                viewPassword()
            elif choice == 2:
                addNewpassword()
            elif choice == 3:
                allpasword()
                

# running the main function
main()


    


