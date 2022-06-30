''' Write a function that takes a string and prints the longest  alphabetical
ordered substring occurred For example, if the string is ' abdulrahman ' then
the output Longest substring in alphabetical order is: abdu '''

def checker(str):
    sub = []
    substring = []
    for letters in str:
        sub = sub + [letters]
        if sub == sorted(sub) and len(sub) >= len(substring):
            substring = sub
        elif sub != sorted(sub):
            sub = [sub[len(sub) - 1]]
    return ''.join(substring)


string = input("Enter any string you want : ")
print("Longest substring in alphabetical order is :", checker(string))
