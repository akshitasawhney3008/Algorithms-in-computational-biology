def naive_pat(str1,str2):
    len1=len(str1)
    len2=len(str2)
   # print(len1,len2)
    if len1>len2:
        print("The string matches at : ", end='')
        for i in range(len1-len2+1):
            count = 0
            for j in range (len2):
                flag=0
                if(str1[i+j]!=str2[j]):
                    count=count+1
                    #print(count)
                    if count>1:
                        break
                else:
                    flag=1

            if j == len2-1 and flag==1:
                list1=[]
                list1=i
                print(str(i), end=' ')
    else:
        for i in range(len2-len1+1):
            for j in range (len1):
                count=0
                if(str2[i+j]!=str1[j]):
                    break
#complexity O(m.n)






















































































































































            if j == len1-1:
                #lst = []
                lst = i
                print(lst)

a=input("Enter a first string")
b=input("Enter a second string")
naive_pat(a,b)
