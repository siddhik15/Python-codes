def print_factors(num):
    if num <= 0:
        print("Invalid input")
        return

    print("Factors are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

num = int(input("Enter a number: "))
print_factors(num)

