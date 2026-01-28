def add_digits(num):
    total = 0
    while num != 0:
        total = total + (num % 10)
        num = num // 10
    return total

number = int(input("Enter a number: "))
result = add_digits(number)
print("Addition of digits:", result)
