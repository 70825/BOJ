def Dijkstra(z):
    q=[];heappush(q,z)
    S=[float('inf')]*n;S[z]=0
    while q:
        x=heappop(q)
        for nx,nt in D[x]:
            if S[nx]>S[x]+nt:
                S[nx]=S[x]+nt;heappush(q,nx)
    ans=0
    for i in range(n):
        if S[i]<=m:ans+=item[i]
    return ans
from heapq import *
n,m,r=map(int,input().split())
item=[*map(int,input().split())]
D=[[] for _ in range(n)]
for i in range(r):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    D[a].append([b,c])
    D[b].append([a,c])
res=0
for i in range(n):
    res=max(res,Dijkstra(i))
print(res)