
def factorial(number):
    # Recursive magic is here
    return number * factorial( number - 1) if number != 1 else 1

number = int(input("Please enter the number: "))

print("The factorial of", number, "is", factorial(number))