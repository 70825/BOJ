def f(x):
    if x==P[x]:return x
    P[x]=f(P[x])
    return P[x]
n,m,k=map(int,input().split())
A=[0]+[*map(int,input().split())]
P=[i for i in range(n+1)]
V=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    x=f(a);y=f(b)
    if A[x]>A[y]: P[x]=y
    else: P[y]=x
ans=0
for i in range(1,n+1):P[i]=f(i)
for i in range(1,n+1):
    x=P[i]
    if V[x]==0:V[x]=1;ans+=A[x]
print(['Oh no',ans][ans<=k])