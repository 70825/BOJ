def edge(A,B,C):
    c[A][B]=1
    d[A][B]=C
    d[B][A]=-C
    path[A].append(B)
    path[B].append(A)
from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
c=[[0]*(2*n) for _ in range(2*n)]
d=[[0]*(2*n) for _ in range(2*n)]
f=[[0]*(2*n) for _ in range(2*n)]
path=[[] for _ in range(2*n)]
for i in range(m):
    x,y,z=map(int,input().split())
    edge(2*(x-1)+1,2*(y-1),z)
    edge(2*(y-1)+1,2*(x-1),z)
for i in range(n):
    x,y=i*2,i*2+1
    c[x][y]=float('inf')
    path[x].append(y)
    path[y].append(x)
S=1;E=2*(n-1)
cost=0
for i in range(2):
    prev=[-1]*(2*n)
    dist=[float('inf')]*(2*n)
    inQ=[0]*(2*n)
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
    if prev[E]==-1:break
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=1
        f[x][nx]-=1
        cost+=d[nx][x]
        x=nx
print(cost)