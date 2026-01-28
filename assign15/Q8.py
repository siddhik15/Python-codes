div_by_3_and_5 = lambda lst: list(filter(lambda x: x % 3 == 0 and x % 5 == 0, lst))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Numbers divisible by both 3 and 5:", div_by_3_and_5(numbers))
