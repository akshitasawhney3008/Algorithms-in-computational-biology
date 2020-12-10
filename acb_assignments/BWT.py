def bwt(s):
    n=len(s)
    m=sorted([s[i:n]+s[0:i] for i in range(n)])
    print(m)
    #print(type(m))
    index =m.index(s)
    print(index)
    #print(type(index))
    l=''.join(q[-1] for q in m)
    print(l)
    F = sorted([l[i] for i in range(n)])
    x=list(F)
    print(x)
    T = [None for i in range(n)]
    for i in range(n):
        j = x.index(l[i])
        print(j)
        T[i] = j
        print(T)
        x[j] = None
        print(x)
    Tx = list([int(index), ])
    print(Tx)
    for i in range(1, n):
        Tx.append(T[Tx[i - 1]])
        print(Tx)
    S = [l[i] for i in Tx]
    S.reverse()
    print(''.join(S))


bwt("abaaba$")