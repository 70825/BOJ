def edge(x,y,z):
    c[x][y]=z
    path[x].append(y)
    path[y].append(x)
from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
nm=n+m+2
S=nm-2;E=S+1
c=[[0]*nm for _ in range(nm)]
f=[[0]*nm for _ in range(nm)]
path=[[] for _ in range(nm)]
J=[*map(int,input().split())]
for i in range(n):
    edge(i,E,10**10)
M=[*map(int,input().split())]
for i in range(m):
    edge(S,i+n,M[i])
for i in range(n,n+m):
    a,*b=map(int,input().split())
    for j in b:
        j-=1
        if 0<=j<n:edge(i,j,J[j])
        else:edge(i,j,M[j-n])
res=0
while 1:
    q=deque([S])
    prev=[-1]*nm
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                prev[nx]=x
                q.append(nx)
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
        x=nx
    res+=flow
print(res)