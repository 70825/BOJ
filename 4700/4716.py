def edge(x,y,z,w=0):
    c[x][y]=z
    path[x].append(y)
    path[y].append(x)
    d[x][y]=w
    d[y][x]=-w

from collections import deque
input=__import__('sys').stdin.readline
while 1:
    n,a,b=map(int,input().split())
    if n==a==b==0:break
    c=[[0]*(n+4) for _ in range(n+4)]
    d=[[0]*(n+4) for _ in range(n+4)]
    f=[[0]*(n+4) for _ in range(n+4)]
    path=[[] for _ in range(n+4)]
    S=n+2;E=S+1
    edge(S,n,a)
    edge(S,n+1,b)
    for i in range(n):
        x,y,z=map(int,input().split())
        edge(i,E,x)
        edge(n,i,x,y)
        edge(n+1,i,x,z)
    cost=0
    while 1:
        q=deque([S])
        prev=[-1]*(n+4)
        dist=[float('inf')]*(n+4)
        inQ=[0]*(n+4)
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
    print(cost)