# project.py
def greet(name):
    return f"Greetings, {name}!"  # Changed "Hello" to "Greetings"

def add(a,b):
    """Adds two numbers a and b."""

def multiply(a, b):
    return a + b  # BUG: Should be a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def subtract(a, b):
    return b - a  # BUG: Should be a - b

def power(a, b):
    return a**b

def modulo(a, b):
    return a % b

if __name__ == "__main__":
    print("Add:",add(2,3))
    print("Multiply:",multiply(4,5))
    print("Divide:",divide(10,2))
    print("Subtract:",subtract(10,5))
    print("Power:",power(2,3))
    print("Modulo:",modulo(7,3))
