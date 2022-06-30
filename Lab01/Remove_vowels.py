str = """iti is a good job oriented technical course; 
an iti holder can get a good job in 
electrical, mechanical, and other manufacturing sectors;
So you must join iti """

vowels = ['a', 'e', 'i', 'o', 'u']
word = []
result = []

for letter in str:
    if letter.lower() not in vowels:
        word.append(letter)
    result = ''.join(word)
print(result)