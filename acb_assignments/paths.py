def paths(m,n):
    if m==0 and n==0:
        return
    elif m==0:
        return 1
    elif n==0:
        return 1
    else:
        return paths(m-1,n)+ paths(m,n-1)
print(paths(0,2))
