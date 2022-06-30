import re
open("data.txt", "a")


def validation(i, e, p, c, m):
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    mob = r'\b01[0-2,5]{1}[0-9]{8}\b'

    if len(i) > 1 and not (i.isdigit()) and re.fullmatch(reg, e) and p == c != "" and re.fullmatch(mob, m):
        return 1
    else:
        return 0


def exist(i, e, m):
    f = open("data.txt", 'r')
    data = f.read()
    if i in data:
        print("Name Unavailable, Please try again with another user name.")
        return 0
    elif e in data:
        print("This mail already exist, try to Login.")
        return 0
    elif m in data:
        print("This mobile number is used before, Please try again with another mobile number.")
        return 0
    else:
        return 1


def register():
    first = input("Enter your first name : ")
    last = input("Enter your last name : ")
    Email = input("Enter valid e-mail : ")
    Pass = input("Enter any password you want : ")
    confirm = input("Enter your password again : ")
    mobile = input("Enter valid mobile phone : ")

    info = " ".join([first, last])

    if validation(info, Email, Pass, confirm, mobile) and exist(info, Email, mobile):
        print("Account has been created successfully. \n")
        data = " : ".join([info, Email, Pass, mobile])
        mydata = open("data.txt", "a")
        mydata.write(data)
        mydata.write("\n")
    else:
        print("Invalid input...!")
