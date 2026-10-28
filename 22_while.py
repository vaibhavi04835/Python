n = int(input("Enter a number: "))
count = 0

n = abs(n)

while n > 0:
    count = count + 1
    n = n // 10

print("Number of digits =", count)