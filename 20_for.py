n=int(input("enter a number:"))
fact=1
if n<0:
    print("factorial is not possible")
else:
    for i in range(1,n+1):
        fact =fact*i
        print("factorial=",fact)
        