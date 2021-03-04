from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
S=n+m;E=S+1
c=[[0]*(n+m+2) for _ in range(n+m+2)]
d=[[0]*(n+m+2) for _ in range(n+m+2)]
f=[[0]*(n+m+2) for _ in range(n+m+2)]
path=[[] for _ in range(n+m+2)]
for i in range(n):
    a,*b=map(int,input().split())
    c[S][i]=1
    path[i].append(S)
    path[S].append(i)
    for j in range(0,len(b),2):
        w,p=b[j],b[j+1]
        w=w-1+n
        c[i][w]=1
        d[i][w]=p
        d[w][i]=-p
        path[i].append(w)
        path[w].append(i)
for i in range(m):
    c[i+n][E]=1
    path[i+n].append(E)
    path[E].append(i+n)
res=0
cost=0
while 1:
    q=deque([S])
    prev=[-1]*(n+m+2)
    dist=[float('inf')]*(n+m+2)
    inQ=[0]*(n+m+2)
    dist[S]=0;inQ[S]=1
    while q:
        x=q.popleft()
        inQ[x]=0
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and dist[nx]>dist[x]+d[x][nx]:
                dist[nx]=dist[x]+d[x][nx]
                prev[nx]=x
                if inQ[nx]==0:q.append(nx);inQ[nx]=1
    if prev[E]==-1:break
    flow=float('inf')
    x=E
    while x!=S:
        nx=prev[x]
        flow=min(flow,c[nx][x]-f[nx][x])
        x=nx
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=flow
        f[x][nx]-=flow
        cost+=flow*d[nx][x]
        x=nx
    res+=1
print(res)
print(cost)