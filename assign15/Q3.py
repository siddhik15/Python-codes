odd_numbers = lambda lst: list(filter(lambda x: x % 2 != 0, lst))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Odd numbers:", odd_numbers(numbers))
