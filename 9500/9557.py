for _ in range(int(input())):
    n=int(input())
    D=[*map(str,input().split())]
    k=-1
    for i in range(n):
        if '#' not in D[i]:k=i
    if k==-1 or len(D)==1:print(' '.join(D))
    else:
        A=' '.join(D[:k:]);B=' '.join(D[k+1::])
        if k==0:print(B,D[k])
        elif k==n-1:print(D[k],A)
        else:print(B,D[k],A)