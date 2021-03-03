from collections import deque
import sys
input=sys.stdin.readline
def go():
    c=[[0]*(2*v+2) for _ in range(2*v+2)]
    d=[[0]*(2*v+2) for _ in range(2*v+2)]
    f=[[0]*(2*v+2) for _ in range(2*v+2)]
    path=[[] for _ in range(v+e+2)]
    for i in range(e):
        x,y,z=map(int,input().split())
        x=(x-1)*2+1
        y=(y-1)*2
        c[x][y]=1
        d[x][y]=z
        d[y][x]=-z
        path[x].append(y)
        path[y].append(x)
    for i in range(v):
        x,y=i*2,i*2+1
        c[x][y]=1
        path[x].append(y)
        path[y].append(x)
    cost=0
    S=1;E=(v-1)*2
    for i in range(2):
        prev=[-1]*(2*v)
        dist=[float('inf')]*(2*v)
        inQ=[0]*(2*v)
        q=deque([S])
        dist[S]=0;inQ[S]=1
        while q:
            x=q.popleft()
            inQ[x]=0
            for nx in path[x]:
                if c[x][nx]-f[x][nx]>0 and dist[nx]>dist[x]+d[x][nx]:
                    dist[nx]=dist[x]+d[x][nx]
                    prev[nx]=x
                    if inQ[nx]==0:q.append(nx);inQ[nx]=1
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
for lines in sys.stdin:
    v,e=map(int,lines.split())
    go()