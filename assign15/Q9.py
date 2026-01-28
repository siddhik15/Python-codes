from functools import reduce

product_all = lambda lst: reduce(lambda a, b: a * b, lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Product of all elements:", product_all(numbers))
