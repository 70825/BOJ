from heapq import *
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
    D[b].append((a,c))
S=[[float('INF')]*(k+1) for _ in range(n+1)]
S[1][0]=0
q=[];heappush(q,(0,0,1))
while q:
    t,e,x=heappop(q)
    if S[x][e]!=t:continue
    for nx,nt in D[x]:
        if e+1<=k and S[nx][e+1]>t:
            S[nx][e+1]=t;heappush(q,(t,e+1,nx))
        if S[nx][e]>nt+t:
            S[nx][e]=nt+t;heappush(q,(t+nt,e,nx))
print(min(S[n]))