from heapq import *
n,m=map(int,input().split())
S=[float('inf')]*(n+1)
D=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    D[a].append(b);D[b].append(a)
q=[];heappush(q,(0,1));S[1]=0
while q:
    t,x=heappop(q)
    if S[x]!=t:continue
    for nx in D[x]:
        if S[nx]>t+1:S[nx]=t+1;heappush(q,(t+1,nx))
ans=[];k=0
for i in range(2,n+1):
    k=max(k,S[i])
for i in range(2,n+1):
    if k==S[i]:ans.append(i)
print(ans[0],k,len(ans))