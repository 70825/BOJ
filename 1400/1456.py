from bisect import bisect
def primelist(n):
    s=[True]*(n+1)
    for i in range(2,int((n)**0.5)+1):
        if s[i]:
            for j in range(i+i,n+1,i):
                s[j]=False
    return [i for i in range(2,n+1) if s[i]]
a,b=map(int,input().split())
D=primelist(10**7)
check=set()
for i in range(len(D)):
    k=D[i]*D[i]
    while k<=b:
        check.add(k)
        k*=D[i]
check=sorted(list(check))
k=bisect(check,a)
if check[k-1]==a:k-=1
print(len(check)-k)