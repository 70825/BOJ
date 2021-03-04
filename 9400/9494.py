while 1:
    T=int(input())
    if T==0:break
    k=0
    for i in range(T):
        S=str(input())+' '
        if len(S)>=k:
            for j in range(k,len(S)):
                if S[j]==' ':k=j;break
    print(k+1)