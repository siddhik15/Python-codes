import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(lst):
    print("Prime Numbers:")
    for num in lst:
        if is_prime(num):
            print(num, end=" ")
    print()

def non_prime_numbers(lst):
    print("Non-Prime Numbers:")
    for num in lst:
        if not is_prime(num):
            print(num, end=" ")
    print()

data = [10, 11, 12, 13, 14, 17, 19, 20]

t1 = threading.Thread(target=prime_numbers, args=(data,), name="Prime")
t2 = threading.Thread(target=non_prime_numbers, args=(data,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()