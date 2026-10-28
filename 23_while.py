n=int(input("enter a number"))
sum=0
n=abs(n)
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
    print("sum of digits=",sum)
    
        