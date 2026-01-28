def count_digits(num):
    count = 0
    while num != 0:
        count = count + 1
        num = num // 10
    return count

number = int(input("Enter a number: "))
result = count_digits(number)
print("Number of digits:", result)
