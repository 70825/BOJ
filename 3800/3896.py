def primelist(n):
    s=[True]*(n+1)
    for i in range(2,int((n)**0.5)+1):
        if s[i]:
            for j in range(i+i,n+1,i):
                s[j]=False
    return [i for i in range(2,n+1) if s[i]]
D=primelist(1299709)
for _ in range(int(input())):
    k=int(input())
    for i in range(len(D)):
        if D[i]>k:print(D[i]-D[i-1]);break
        if D[i]==k:print(0);break