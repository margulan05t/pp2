def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        even_nums = even_numbers(n)
        print("Even numbers between 0 and", n, ":", end=" ")
        print(*even_nums, sep=", ", end="\n")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
