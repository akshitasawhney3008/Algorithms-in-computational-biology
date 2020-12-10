list1=[]
item=input("Enter the  Items to the list")
list1.append(item)
i=0
j=len(list1)
print(j)
while i<j:
    minm =min(list1[i:])
    print (minm)
    indx_of_min=list1.index(minm)
    print(indx_of_min)
    list1[indx_of_min],list1[i]=list1[i],list1[indx_of_min]
    i=i+1
print(list1)


