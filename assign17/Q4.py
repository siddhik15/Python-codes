def add_factors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total = total + i
    return total

number = int(input("Enter a number: "))
result = add_factors(number)
print("Addition of factors is:", result)
