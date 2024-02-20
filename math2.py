import math

def area(a, b, h):
    area = 0.5 * (a + b) * h
    return area

a = float(input("Input a: "))
b = float(input("Input b: "))
h = float(input("Input h: "))

result = area( a, b, h)
print("Area is:", result)
