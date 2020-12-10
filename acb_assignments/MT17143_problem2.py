#c is the money of the item
#n is the number of items
#w is the mass of the item
#mc is the max weight of the knapsack

def knapsack(n,c,w,mc):

    if n==0 or mc==0:
        return 0

    if int(w[n])>mc:
        return knapsack(n-1,c,w,mc)
    else:
        c1=knapsack(n - 1,c,w, mc),
        c2=knapsack(n - 1,c,w,(mc - int(w[n-1])))+ int(c[n-1])
       # print(c2)
        return max(c1[0],c2)


# def max(a,b):
#     if a>b:
#         max=a
#     else:
#         max=b
#     return(max)

cost=[]
weight=[]
cw=[]
n=int(input("enter the no. of items"))
for i in range (n):
    lst=input().split(' ')
    cw.append(lst)
 #   print(cw.index(lst))
for row in range (len(cw)):
    #for col in range (len(cw[i])):
        cost.append(cw[row][0])
        weight.append(cw[row][1])
m=0
#print(type(max))
for el in weight:
    m+=int(el)
print(knapsack(n-1,cost,weight,m))

#max=sum(i for i in weight)


#x=[x for x in cw][0]
#cost=x.index(1)
#weight=cw[1]
#print(cost)


