def pascal(col,row):
    if col==0 or col==row:
        return 1
    if row==0:
        return 0
    else:
        return pascal(col-1,row-1)+ pascal(col,row-1)

def pascal_tri(n):
    if n<=0:
        print("should me more than 0")
    else:
        for r in range (n):
            for c in range (r+1):
                print(str(pascal(c,r)),end=' ')
            print('\n')


n=int(input("Enter the number of rows"))
pascal_tri(n)
