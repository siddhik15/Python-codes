count_even = lambda lst: len(list(filter(lambda x: x % 2 == 0, lst)))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Count of even numbers:", count_even(numbers))
