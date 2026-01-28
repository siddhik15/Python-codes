import threading

def even_numbers():
    print("Even Thread Started")
    for i in range(2, 21, 2):
        print("Even :", i)

def odd_numbers():
    print("Odd Thread Started")
    for i in range(1, 20, 2):
        print("Odd :", i)

even = threading.Thread(target=even_numbers, name="Even")
odd = threading.Thread(target=odd_numbers, name="Odd")

even.start()
odd.start()

even.join()
odd.join()

print("Main thread exiting")