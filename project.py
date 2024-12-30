# project.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(greet("World"))
    print(add(2, 3))
    print(multiply(4, 5))
    print(divide(10, 2))