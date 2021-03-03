from heapq import *
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
k=int(input())
D=[[] for _ in range(n+1)]
S=[float('INF')]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
S[k]=0;q=[];heappush(q,[0,k])
while q:
    t,x=heappop(q)
    for i in range(len(D[x])):
        nt,nx=t+D[x][i][1],D[x][i][0]
        if S[nx]>nt:S[nx]=nt;heappush(q,[nt,nx])
for i in range(1,n+1):
    print(['INF',S[i]][S[i]<10**10])