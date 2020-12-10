def hcf(m,n):
    a=1
    while a!=0:
        if m>n:
            a=m%n
            m=n
            n=a
            b=m

        else:
            a=n%m
            n=m
            m=a
            b=n
    return b
m=int(input("Enter the first num"))
n=int(input("Enter the second num"))
print(hcf(m,n))


