import math

def area(a,b):
    area = a*b
    return area

a = float(input("Length of base:"))
b = float(input("Heigh of parallelogram:"))

result = area(a,b)
print("Area of parallelogram is:", result)