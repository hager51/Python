str = """iti is a good job oriented technical course; 
        an iti holder can get a good job in 
        electrical, mechanical, and other manufacturing sectors;
        So you must join iti """

a = str.split(" ")
sub = "iti"
count = 0

for i in range(0, len(a)):
    if sub == a[i]:
        count += 1

print(count)
