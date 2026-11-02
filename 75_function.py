def prime(n):
    if n <= 1:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                return
        print("Prime Number")

prime(7)