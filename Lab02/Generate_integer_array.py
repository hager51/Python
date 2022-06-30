''' Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start. '''

def generateArr(L, S):
    arr = []
    for i in range(0, L):
        arr.append(S)
        S += 1

    return arr


Len = int(input("Enter length of array : "))
Start = int(input("Enter Start element of array : "))

print(generateArr(Len, Start))
