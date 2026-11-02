def largest(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)

largest(10, 25, 15)