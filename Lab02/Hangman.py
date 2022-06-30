import random

name = input("What is your name? ")
print("Welcome In Word Guessing Game, Good Luck ", name)

words = ["hager", "mohamed", "ahmed", "heba", "ghada", "ali",
         "taha", "yara", "hader", "eslam", "mostafa", "khalid"]

word = random.choice(words)
guesses = ''
turns = 7

while turns > 0:

    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("*")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
