import threading

def display_forward():
    print("Thread1 Started")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 Completed")

def display_reverse():
    print("Thread2 Started")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 Completed")

t1 = threading.Thread(target=display_forward, name="Thread1")
t2 = threading.Thread(target=display_reverse, name="Thread2")

t1.start()
t1.join()   # Thread2 waits for Thread1 to finish

t2.start()
t2.join()

print("Main thread exiting")