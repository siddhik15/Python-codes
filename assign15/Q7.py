long_strings = lambda lst: list(filter(lambda s: len(s) > 5, lst))

strings = input("Enter strings separated by space: ").split()

print("Strings with length greater than 5:", long_strings(strings))
