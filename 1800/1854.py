from heapq import *
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[[] for _ in range(n+1)]
S=[[float('inf')]*k for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
q=[];heappush(q,(0,1))
S[1][0]=0
while q:
    t,x=heappop(q)
    for nx,nt in D[x]:
        if nt+t < S[nx][k-1]:
            S[nx][k-1]=nt+t;S[nx].sort();heappush(q,(nt+t,nx))
for i in range(1,n+1):
    print(-1 if S[i][k-1]==float('inf') else S[i][k-1])