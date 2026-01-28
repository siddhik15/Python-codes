import threading

def find_max(lst):
    print("Maximum Element:", max(lst))

def find_min(lst):
    print("Minimum Element:", min(lst))

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

t1 = threading.Thread(target=find_max, args=(lst,))
t2 = threading.Thread(target=find_min, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()