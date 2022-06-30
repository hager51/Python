''' Write a program which repeatedly reads numbers until the user enters “done”. '''

num = 0
tot = 0.0
while True:
    number = input("Enter any number you want : ")
    if number == "done":
        break
    elif number.isdigit():
        tot += float(number)
    else:
        print('Invalid Input')
        continue
    num += 1

print("Program Done")
print("Total = ", tot)
print("Count = ", num)
print("Average = ", tot/num)
