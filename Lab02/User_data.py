''' Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for his
email and print all this data, check if it is a valid email or not '''

import re

name = input("Enter your name please : ")
Email = input("Enter your e-mail please : ")

reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if len(name) > 0 and not(name.isdigit()) and re.fullmatch(reg, Email):
    print("Your name is : ", name)
    print("your e-mail is : ", Email)
else:
    print("Invalid input...!")
