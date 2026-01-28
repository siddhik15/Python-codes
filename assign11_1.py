def CheckPrime(n):
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break

    if n > 1 and flag == 0:
        print("Prime number")
    else:
        print("Not a prime number")

CheckPrime(9)
