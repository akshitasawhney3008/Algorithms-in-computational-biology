t=int(input("Enter the number of test cases"))

while t!=0:
    str1=input("enter the string")
    t=t-1
    if str1[0]== '[':
        i=1
        while i<(len(str1)-1):
            print(str1[i],end='')
            i+=1


      #  str2= str1
       # list=str1.split()
       # print(list)
       # str2 =','.join(list)
       # print("'%s'" %str2)
    #elif isinstance(str1, list):
     #   my_list = ', '.join(str1)
      #  print("'%s'" % (my_list))
       # print(type(str1))
   # elif isinstance(str1, dict):
    #    for v in str1.values():
           # dic = v
     #   print("'%s'" % (dic), end=',')
      #  print(type(str1))
    #else:
     #   print("'x'")
