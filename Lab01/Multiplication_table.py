num = int(input("Enter any number you want to calculate multiplication table till it : "))
result = []

for i in range(1, num+1):
    x = []
    
    for j in range(1, i+1):
        x.append(i*j)
    
    result.append(x)

print(result)