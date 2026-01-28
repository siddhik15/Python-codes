import threading

def even_list(lst):
    evens = [i for i in lst if i % 2 == 0]
    print("Even Elements:", evens)
    print("Sum of Even Elements:", sum(evens))

def odd_list(lst):
    odds = [i for i in lst if i % 2 != 0]
    print("Odd Elements:", odds)
    print("Sum of Odd Elements:", sum(odds))

data = [10, 15, 20, 25, 30, 35]

t1 = threading.Thread(target=even_list, args=(data,), name="EvenList")
t2 = threading.Thread(target=odd_list, args=(data,), name="OddList")

t1.start()
t2.start()

t1.join()
t2.join()