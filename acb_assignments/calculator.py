#def calci(a,b,ch):
a=int(input("Enter a first number"))
b=int(input("Enter a second number"))
ch1=(input("Enter the operation 0:'+',1:'-',2:'*',3:'/',4:'//',5:'**'"))
ch={
        '0': a+b,
        '1': a-b,
        '2': a*b,
        '3': a/b,
        '4': a//b,
        '5': a**b
    }
print(ch[ch1])