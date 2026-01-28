from functools import reduce

max_element = lambda lst: reduce(lambda a, b: a if a > b else b, lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Maximum element:", max_element(numbers))
