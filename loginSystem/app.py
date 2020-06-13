first_name = ""
last_name = ""
username = "admin"
email = ""
password = "root"

def route():
    register()

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
            def redirect():
                temp = input("Do you want to create an account (y or n)? : ")
                if temp.lower() == "y":
                    register()
                elif temp.lower() == "n":
                    getLoginInfo()
                else:
                    print("The computer didn't understand")
                    redirect()

    else:
        print("wrong username")



def register():
    print("Welcome to Create a account!")
    global first_name
    global last_name
    global username
    global email
    global password

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    temp = input("Do you want to login now (y or n)? : ")
    if temp.lower() == "y":
        getLoginInfo()
    elif temp.lower() == "n":
        print("no no")
    else:
        print("The computer didn't understand")



route()