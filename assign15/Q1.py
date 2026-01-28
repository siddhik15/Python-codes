squares = lambda lst: list(map(lambda x: x * x, lst))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Squares of numbers:", squares(numbers))
