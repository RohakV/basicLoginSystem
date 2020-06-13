first_name = ""
last_name = ""
username = "a"
email = ""
password = "r"

def route():
    getLoginInfo()

def getLoginInfo():
    print("Welcome to login")
    print("Remember, everything is case sensitive!")
    global l_uid
    global l_pswd
    l_uid = input("Enter your username: ")
    l_pswd = input("Enter your password: ")
    check()
    
def check():
    if l_uid == username:
        if l_pswd == password:
            print("You are in")
        else:
            print("wrong password")
    else:
        print("wrong username")


route()