first_name = ""
last_name = ""
username = ""
email = ""
password = ""

def route():
    getLoginInfo()

def getLoginInfo():
    print("Welcome to login")
    print("Remember, Everything is Case Sensitive!")
    global l_uid
    global l_pswd
    l_uid = input("Enter your username: ")
    l_pswd = input("Enter your password: ")
    
def check():
    


route()