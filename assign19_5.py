from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [2, 70, 11, 10, 17, 23, 31, 77]

# Filter prime numbers
filtered = list(filter(is_prime, numbers))

# Multiply each by 2
mapped = list(map(lambda x: x * 2, filtered))

# Maximum number
result = reduce(lambda a, b: a if a > b else b, mapped)

print("List after filter:", filtered)
print("List after map:", mapped)
print("Output of reduce:", result)