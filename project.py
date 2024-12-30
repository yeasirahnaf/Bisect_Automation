# project.py
def greet(name):
    return f"Greetings, {name}!"  # Changed "Hello" to "Greetings"

def add(a, b):
    return a + b

def multiply(a, b):
    return a + b  # BUG: Should be a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def power(a, b):
    return a**b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print(add(2, 3))
    print(multiply(4, 5))
    print(divide(10, 2))
    print(subtract(10, 5))
    print(power(2,3))