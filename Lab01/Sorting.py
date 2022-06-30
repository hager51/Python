array = []
n = 5

for i in range(0, 5):
	a = input("Enter element number %d: " % (i+1))
	array.append(a)
	
array.sort()
print("ascending order : ")
for i in range(0, 5):
	print(array[i])

print("descending order : ")
array.reverse()
for i in range(0, 5):
	print(array[i])