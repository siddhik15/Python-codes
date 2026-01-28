def print_reverse(n):
    if n <= 0:
        print("Invalid input")
        return

    for i in range(n, 0, -1):
        print(i)

n = int(input("Enter a number: "))
print_reverse(n)
