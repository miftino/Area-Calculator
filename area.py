import math

# Asks user to pick what shape 
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
shape = int(input("Enter your choice: "))
print("")


# If they pick square
if shape == 1:
    side = float(input("Enter legth of side: "))
    area = side ** 2
    print("Area:", area)

# If they pick Rectangle
elif shape == 2:
    length = float(input("Enter the length: "))
    width  = float(input("Enter the width: "))
    area = length * width
    print("Area:", area)

# If they pick Triangle
elif shape == 3:
    height = float(input("Enter the height: "))
    base  = float(input("Enter the base: "))
    area = (height * base)/2
    print("Area:", area)

# If they pick Circle
elif shape == 4:
    radius = float(input("Enter the radius: "))
    area = (radius ** 2) * math.pi
    print("Area:", area)

# If they did not pick 1 through 4
else:
    print("Please enter a number 1 through 4")


