import math

def area_of_regular_polygon(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

result = area_of_regular_polygon(n, s)
print("The area of the polygon is:", result)
