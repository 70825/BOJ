from heapq import *
input=__import__('sys').stdin.readline
n,m=int(input()),int(input())
D=[[] for _ in range(n+1)]
S=[float('INF')]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    D[a].append((b,c))
s,e=map(int,input().split())
q=[];heappush(q,[0,s])
while q:
    t,x=heappop(q)
    for nx,nt in D[x]:
        if S[nx]>nt+t:S[nx]=nt+t;heappush(q,[nt+t,nx])
print(S[e])