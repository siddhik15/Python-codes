from functools import reduce

add_all = lambda lst: reduce(lambda a, b: a + b, lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Addition of all elements:", add_all(numbers))
