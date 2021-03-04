from heapq import *
Max=float('Inf')
n,r=map(int,input().split())
D=[[] for _ in range(n+1)]
for i in range(r):
    a,b,c,d,e=map(int,input().split())
    if e<=10:D[a].append((b,c))
    else:D[a].append((b,c+(e-10)*d))
S=[[Max]*(n+1) for _ in range(n+1)];S[1][1]=0
q=[];heappush(q,[0,1,1])
while q:
    t,e,x=heappop(q)
    if S[x][e]!=t:continue
    for nx,nt in D[x]:
        if e<n and S[nx][e+1]>nt+t:
            S[nx][e+1]=nt+t;heappush(q,[nt+t,e+1,nx])
k=min(S[n])
if k==Max:print('It is not a great way.')
else:
    for i in range(n+1):
        if S[n][i]==k:print(k,i);break