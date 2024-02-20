def divisible_by_three_and_four_generator():
    n = int(input("Enter the value of n: "))
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


result_generator = divisible_by_three_and_four_generator()

for number in result_generator:
    print(number)

            