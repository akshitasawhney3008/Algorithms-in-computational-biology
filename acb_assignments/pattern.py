for i in range(5):
    j=i
    while(j):
        print("*",end='')
        j-=1
    print("")
for i in range(5,0,-1):
    j=1
    while(j<i):
        print("*", end='')
        j+=1
    print("")
