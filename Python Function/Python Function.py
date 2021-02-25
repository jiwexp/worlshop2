def add(number1, number2):
    return number1 + number2


def substract(number1, number2):
    return number1 - number2


def multyple(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

print(f"{number1} + {number2} = {(add(number1, number2))}")
print(f"{number1} + {number2} = {(substract(number1, number2))}")
print(f"{number1} + {number2} = {(multyple(number1, number2))}")
print(f"{number1} + {number2} = {(divide(number1, number2))}")