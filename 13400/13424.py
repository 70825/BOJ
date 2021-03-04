def Dijkstra():
    while q:
        t,x=heappop(q)
        if S[x]!=t:continue
        for nx,nt in D[x]:
            if S[nx]>t+nt:
                S[nx]=t+nt;heappush(q,[t+nt,nx])
from heapq import *
for _ in range(int(input())):
    n,m=map(int,input().split())
    D=[[] for _ in range(n+1)]
    ans=[0]*(n+1)
    for i in range(m):
        a,b,c=map(int,input().split())
        D[a].append((b,c))
        D[b].append((a,c))
    k=int(input())
    K=[*map(int,input().split())]
    for i in range(k):
        S=[float('inf')]*(n+1);S[K[i]]=0
        q=[];heappush(q,[0,K[i]])
        Dijkstra()
        for j in range(n+1):
            ans[j]+=S[j]
    z=min(ans)
    for i in range(1,n+1):
        if z==ans[i]:print(i);break