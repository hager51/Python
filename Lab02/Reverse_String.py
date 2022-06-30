''' Write a function which has an input of a string from user then it
will return the same string reversed. '''

def reverse_string(str):
    return str[::-1]


string = input("Enter string you want to reverse : ")
print(reverse_string(string))
