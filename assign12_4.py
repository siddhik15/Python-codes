def print_numbers(n):
    if n <= 0:
        print("Invalid input")
        return

    for i in range(1, n + 1):
        print(i)

n = int(input("Enter a number: "))
print_numbers(n)
