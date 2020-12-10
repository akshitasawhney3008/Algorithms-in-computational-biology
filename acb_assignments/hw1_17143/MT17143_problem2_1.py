def kmers(l,pre,n,k):
    prefix=""
    if k==0:
        print(pre,end=',')
        return
    else:
        for i in range (0,n):
            prefix=pre+l[i]
            kmers(l,prefix,n,k-1)


letters=['-','A','G','C','T']
n=len(letters)
k=int(input("enter the value of k"))
kmers(letters,"",n,k)
