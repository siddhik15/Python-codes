
import threading

def even_factors(n):
    sum_even = 0
    print("Even Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum_even += i
    print("\nSum of Even Factors:", sum_even)

def odd_factors(n):
    sum_odd = 0
    print("Odd Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum_odd += i
    print("\nSum of Odd Factors:", sum_odd)

num = int(input("Enter number: "))

t1 = threading.Thread(target=even_factors, args=(num,), name="EvenFactor")
t2 = threading.Thread(target=odd_factors, args=(num,), name="OddFactor")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")