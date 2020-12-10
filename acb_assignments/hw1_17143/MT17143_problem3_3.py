def kmparray(pat):
    l = len(pat)
    # for i in range (l):
    kmp1 = [None] * (l)
    kmp1[0] = 0
    j = 0
    i = 1
    while (i < l):
        if pat[i] == pat[j]:
            kmp1[i] = j + 1
            i += 1
            j += 1
        elif j > 0 and pat[i] != pat[j]:
            j = kmp1[j - 1]
        else:
            kmp1[i] = 0
            i = i + 1
    return (kmp1)


def kmp(text, pattern):
    arr = kmparray(pattern)
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    while (i < n and j < m):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif i > 0 and arr[i] == 0:
            j = 0
            i = i + 1
        else:
            i = i - arr[i]
            j = 0
        if (j == len(pattern)):
            print("pattern occurs at " + str(i - j))
            j = 0


text = input("Enter the text")
pattern = input("Enter the pattern")
kmp(text, pattern)
# print(str(kmp(text,pattern)))
#complexity= O(m+n)