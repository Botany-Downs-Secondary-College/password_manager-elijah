#PassowrdManager.py
#This program will manage users passwords

name = ""
passwords_list = []
members_list = []

def menu(name):

    print("Hey there", name)
    mode = input("""Choose whether you would to like add/remove a password(1), view passwords(2) or exit application(3), """).strip()
    return mode

    

def addpassword():
    repeat = True
    while repeat == True:
        password = input("Enter your password, password must include one capital letter and one number, it must also be greater than 8 characters, type end to return to homepage")
        if (any(passreqr.isupper() for passreqr in password) and any(passreqr.isdigit() for passreqr in password) and len(password) >=8):
            passwords_list.append(password)
            print(password, "has been added")
        elif password == "end":
            break
        else:
            print("Your password did not meet the minimum requirements")

    print("Welcome to the password manager")

name = input("What is your name")

while True:
    member = input("Enter 'L' for login or 'N' to create a new account").upper()

    if member == "L":
        m_username = input("Enter your username: ")
        m_password = input("Enter your password:")
        if m_username == "bdsc" and m_password =="Pass1234":
            print("username password match!!")
            break
        else:
            print("Incorrect password, please try again")
    elif member == "N":
        m_username = input("Enter your new account name")
        while True:
            m_password = input("Create password with at least 8 characters, 1 Capital letter and a number:").strip()
            if (any(passreqr.isupper() for passreqr in m_password) and any(passreqr.isdigit() for passreqr in m_password) and len(m_password) >=8):
                members_list.append([m_username,m_password])
                print("Account created :)")
            break


while True:
    chosen_option = menu(name)

    if chosen_option == "1":
        addpassword()
        print("Success!")

    elif chosen_options == "2":
        print("Success!")
        print(passwords_list)

    elif chosen_option == "3":
        break

    else:
        print("Invaild option, try again")




    
