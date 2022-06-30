count = 0
vowels = ['a','e','i','o','u']
arr = input("Enter any string you want : ")
for i in arr:
    if i in vowels:
        count += 1
print (count)