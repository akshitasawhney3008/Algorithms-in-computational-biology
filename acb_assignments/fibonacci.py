#n=0
#def fibo(n):
sum=0
n=int(input("Enter the range of fibonacci series"))
a=0
b=1
print(a)
print(b)
while n>0:
    sum=a+b
    a=b
    b=sum
    print(sum)
    n=n-1