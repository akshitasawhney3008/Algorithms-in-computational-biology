def naive_pat(str1,str2):
    len1=len(str1)
    len2=len(str2)
   # print(len1,len2)
    if len1>len2:
        print("The string matches at :", end='')
        for i in range(len1-len2+1):
            for j in range (len2):
                flag=0
                if(str1[i+j]!=str2[j]):
                    break
                else:
                    flag=1
            if j == len2-1 and flag==1:
                #list=[]
                #list=i
                print(str(i), end=' ')
    else:
        print("The string matches at :", end='')
        for i in range(len2-len1+1):
            for j in range (len1):
                flag=0
                if(str2[i+j]!=str1[j]):
                    break
                else:
                    flag=1
            if j == len1-1 and flag==1:
                #lst = []
               # lst = i
                print(str(i), end=' ')

a=input("Enter a first string")
b=input("Enter a second string")
naive_pat(a,b)
#complexity O(m.n)

