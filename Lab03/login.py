from project import *
def auth(email, password):
    try:
        f = open("data.txt", 'r')
    except FileNotFoundError:
        return "This Email not found, Please register first."
    else:
        data = f.read()
        data = data.split(" : ")
        if email in data:
            index = data.index(email) + 1
            usr_password = data[index]
            if usr_password == password:
                print("Welcome Back, " + email.split('@')[0])
                print("\nOptions: c:Create | v:View | e:Edit | d:delete | s:Search | b:Back")
                print("""
                    Choose c for create a new project.
                    Choose v for see all current projects.
                    Choose e for edit any of your projects.
                    Choose d for delete any of your projects.
                    Choose s for search for a project.
                    Choose b to back to home page.
                    """)
                while True:
                    option = input("Enter your option : ")
                    if option == "c":
                        create(email)
                    elif option == "v":
                        view()
                    elif option == "e":
                        edit(email)
                    elif option == 'd':
                        delete(email)
                    elif option == 's':
                        search()
                    elif option == 'b':
                        return "Welcome to the Crowd-Funding console app.\n" + "Options: r:Register | l:Login | e:Exit\n"
                        break
                    else:
                        return option + " is not an option"
            else:
                return "Password entered is wrong, Please try again\n"
        else:
            return "This Email not found, Please register first.\n"


def login():
    while True:
        mail = str(input("Email: "))
        if not len(mail) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = str(input("Password: "))
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break
    print(auth(mail, password))
