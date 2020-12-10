def fact(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i=i+1
    return fact
n = int(input("Enter a num"))
print(fact(n))