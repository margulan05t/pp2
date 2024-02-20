def squares(a, b):
    for i in range(a, b):
        yield i ** 2

a = 1
b = 6
for square in squares(a, b):
    print(square)
