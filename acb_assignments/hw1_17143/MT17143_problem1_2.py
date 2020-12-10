def trans(s):
    list_of_char = list(s)
    length = len(list_of_char)
    for i in range(0, length):
        if list_of_char[i] == 'T':
            list_of_char[i] = 'U'
    print(''.join(list_of_char))

    #l=len(s)
    #str1=''
    #for i in range(l):
    #    if s[i]=='A':
    #        str1=str1+'U'
    #    if s[i]=='T':
    #        str1=str1+'A'
    #    if s[i]=='G':
    #        str1 = str1 + 'C'
    #    if s[i]=='C':
    #        str1= str1 + 'G'
    #print(str1)


str=(input("Enter the sequence that has to be transcribed"))
trans(str)