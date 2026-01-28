def chk_perfect(num):
    if num <= 0:
        print("Invalid input")
        return

    sum_factors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_factors += i

    if sum_factors == num:
        print("Perfect number")
    else:
        print("Not a perfect number")

num = int(input("Enter a number: "))
chk_perfect(num)
