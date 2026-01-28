import threading

sum_result = 0
product_result = 1

def calculate_sum(lst):
    global sum_result
    sum_result = sum(lst)

def calculate_product(lst):
    global product_result
    for num in lst:
        product_result *= num

lst = [1, 2, 3, 4, 5]

t1 = threading.Thread(target=calculate_sum, args=(lst,))
t2 = threading.Thread(target=calculate_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum of Elements:", sum_result)
print("Product of Elements:", product_result)