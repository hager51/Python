''' write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return " FizzBuzz '''

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = "Invalid input ..."

    return result


number = int(input("Enter the number you want to check : "))

print(fizz_buzz(number))