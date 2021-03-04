from heapq import *
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[[] for _ in range(n)]
S=[float('inf')]*n
for i in range(m):
    a,b,c=map(int,input().split())
    D[b-1].append([a-1,c])
q=[]
K=[*map(int,input().split())]
for i in range(k):
    heappush(q,[0,K[i]-1])
    S[K[i]-1]=0
while q:
    t,x=heappop(q)
    if S[x]!=t:continue
    for nx, nt in D[x]:
        if S[nx]>nt+t:
            S[nx]=nt+t
            heappush(q,[nt+t,nx])
ans=0
res=0
for i in range(n):
    if S[i]>ans:ans=S[i];res=i
print(res+1)
print(ans)