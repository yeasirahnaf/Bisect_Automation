# project.py
def greet(name):
    return f"Greetings, {name}!"  # Changed "Hello" to "Greetings"

def add(a,b):
    """Adds two numbers"""

def multiply(a, b):
    return a + b  # BUG: Should be a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def subtract(a, b):
    return a - b

def power(a, b):
    return a**b

def modulo(a, b):
    return a % b

if __name__ == "__main__":
    print(add(2,3)) #5
    print(multiply(4,5)) #20
    print(divide(10,2)) #5.0
    print(subtract(10,5)) #5
    print(power(2,3)) #8
    print(modulo(7,3)) #1
