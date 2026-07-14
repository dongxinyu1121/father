

def add(a, b, c):
    return a + b + c

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    result = add(3, 5, 2)
    print(f"The sum of 3, 5, and 2 is: {result}")

    result = subtract(10, 4)
    print(f"The difference of 10 and 4 is: {result}")

    result = multiply(6, 7)
    print(f"The product of 6 and 7 is: {result}")

    result = divide(20, 4)
    print(f"The quotient of 20 and 4 is: {result}")
