import math

def calculate_square_area():
    side = float(input("Enter the length of the side: "))
    return side ** 2

def calculate_rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return length * width

def calculate_triangle_area():
    height = float(input("Enter the height: "))
    base = float(input("Enter the base: "))
    return (height * base) / 2

def calculate_circle_area():
    radius = float(input("Enter the radius: "))
    return (radius ** 2) * math.pi

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Arithmetic Operations")
    shape = int(input("Enter your choice: "))
    print("")

    if shape == 1:
        area = calculate_square_area()
        print("Area:", area)
    elif shape == 2:
        area = calculate_rectangle_area()
        print("Area:", area)
    elif shape == 3:
        area = calculate_triangle_area()
        print("Area:", area)
    elif shape == 4:
        area = calculate_circle_area()
        print("Area:", area)
    elif shape == 5:
        print("Arithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operation = int(input("Enter your choice: "))
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if operation == 1:
            print("Result:", add(a, b))
        elif operation == 2:
            print("Result:", subtract(a, b))
        elif operation == 3:
            print("Result:", multiply(a, b))
        elif operation == 4:
            print("Result:", divide(a, b))
        else:
            print("Invalid operation choice.")
    else:
        print("Please enter a number 1 through 5.")

if __name__ == "__main__":
    main()