import datetime

def datevalidate(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d')
        return 0
    except ValueError:
        return 1


def create(mail):
    print("To create a project fund raise campaign you should enter this information...")
    while True:
        title = input("Enter your project name/title : ")
        if not len(title) > 0:
            print("Title can't be blank")
        else:
            break
    while True:
        details = input("Enter the description to this project : ")
        if not len(details) > 0:
            print("Details can't be blank")
        else:
            break
    while True:
        target = input("Enter the total target you need : ")
        if not len(target) > 0:
            print("Target can't be blank")
        else:
            break
    while True:
        start = input("Set start time for the campaign in this format YYYY-MM-DD : ")
        if not len(start) > 0:
            print("Start can't be blank")
        elif datevalidate(start):
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break
    while True:
        end = input("Set end time for the campaign in this format YYYY-MM-DD : ")
        if not len(end) > 0:
            print("End can't be blank")
        elif datevalidate(end):
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break
    print("Your project has been created successfully. \n")
    data = ":".join([mail, title, details, target, start, end])
    pdata = open("PData.txt", "a")
    pdata.write(data)
    pdata.write("\n")


def view():
    try:
        f = open("PData.txt", 'r')
    except FileNotFoundError:
        return "There is no projects tell yet"
    else:
        data = f.read()
        print(data)

def delete(mail):
    flag = 0
    search_text = input("What the name/title of project you want to delete : ")
    with open("PData.txt", "r") as f:
        lines = f.readlines()
    with open("PData.txt", "w") as f:
        for line in lines:
            if mail in line and search_text in line:
                flag = 1
            else:
                f.write(line)
    if flag == 0:
        print("This is not allow, because this is not your project")
    else:
        print("project deleted Successfully.")


def edit(mail):
    old = input("What data you want to edit : ")
    new = input("Enter the new data : ")
    flag = 0
    with open("PData.txt", "r") as f:
        lines = f.readlines()
    with open("PData.txt", "w") as f:
        for line in lines:
            if mail in line and old in line:
                arr = line.split(":")
                f.write(line.replace(arr[arr.index(old)], new))
                flag = 1
            else:
                f.write(line)
    if flag == 0:
        print("This is not allow, because this is not your project")
    else:
        print("project Edit Successfully.")

def search():
    search_text = input("Enter the End date of projects you search about : ")
    searchfile = open("file.txt", "r")
    for line in searchfile:
        if search_text in line:
            print(line)
    searchfile.close()
