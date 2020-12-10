def palindrome(str):
    str=input("Enter a string")
    revstr=''
    index=len(str)
    while index>0:
        revstr+=str[index-1]
        index=index-1
    if(revstr==str):
        str1="It is a palindrome"
    else:
        str1="Not a palindrome"
    return str1
print(palindrome(str))

