from collections import deque
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,m=map(int,input().split())
    nm=2*(n+1)
    c=[[0]*nm for _ in range(nm)]
    d=[[0]*nm for _ in range(nm)]
    f=[[0]*nm for _ in range(nm)]
    path=[[] for _ in range(nm)]
    S=nm-2;E=S+1
    for i in range(n):
        a,b=i*2,i*2+1
        c[S][a]=1
        path[S].append(a)
        path[a].append(S)
        c[b][E]=1
        path[b].append(E)
        path[E].append(b)
        c[a][b]=1
        path[a].append(b)
        path[b].append(a)
        d[a][b]=-1
        d[b][a]=1
    for i in range(m):
        a,b=map(int,input().split())
        a=2*(a-1)+1;b=2*(b-1)
        c[a][b]=1
        path[a].append(b)
        path[b].append(a)
    cost=0
    for i in range(2):
        q=deque([S])
        prev=[-1]*nm
        dist=[float('inf')]*nm
        inQ=[0]*nm
        dist[S]=0;inQ[S]=1
        while q:
            x=q.popleft()
            inQ[x]=0
            for nx in path[x]:
                if c[x][nx]-f[x][nx]>0 and dist[nx]>dist[x]+d[x][nx]:
                    dist[nx]=dist[x]+d[x][nx]
                    prev[nx]=x
                    if inQ[nx]==0:q.append(nx);inQ[nx]=1
        x=E
        while x!=S:
            nx=prev[x]
            f[nx][x]+=1
            f[x][nx]-=1
            cost+=d[nx][x]
            x=nx
    print(-cost)