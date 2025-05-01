def addNumbers(num1, num2):
    return num1 + num2

def subtractNumbers(num1, num2):
    return num1 - num2

def multiplyNumbers(num1, num2):
    return num1 * num2

def divideNumbers(num1, num2):
    if num2 == 0:
        raise "Error: Division by zero is not allowed."
    return num1 / num2