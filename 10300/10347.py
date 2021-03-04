S='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while 1:
    A=input().split()
    if A[0]=='0':break
    a,b=A[0],A[1]
    a=int(a)
    b=[*b]
    for i in range(len(b)):
        k=S.find(b[i])+a
        if k>27:k-=28
        b[i]=S[k]
    print(''.join(b[::-1]))