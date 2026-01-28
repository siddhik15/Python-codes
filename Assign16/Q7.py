def CheckDivisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
result = CheckDivisible(number)
print(result)
