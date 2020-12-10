def digitsum(num):
    num1=0
    while num!=0:
        num1+=num%10
        num = num // 10
    return num1
num=int(input("Enter a number"))
print(digitsum(num))