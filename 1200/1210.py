def edge(x,y,z=float('inf')):
    c[x][y]=z
    path[x].append(y)
    path[y].append(x)
from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
nm=2*n
c=[[0]*nm for _ in range(nm)]
f=[[0]*nm for _ in range(nm)]
path=[[] for _ in range(nm)]
S,E=map(int,input().split())
S=2*(S-1)+1;E=2*(E-1)
pay=[int(input()) for _ in range(n)]
for i in range(n):
    edge(2*i+1,2*i,pay[i])
for i in range(m):
    x,y=map(int,input().split())
    x-=1;y-=1
    edge(2*x,2*y+1)
    edge(2*y,2*x+1)
res=0
while 1:
    prev=[-1]*nm
    q=deque([S])
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                prev[nx]=x;q.append(nx)
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
visited=[0]*nm
visited[S]=1
q=deque([S])
while q:
    x=q.popleft()
    for nx in path[x]:
        if c[x][nx]-f[x][nx]>0 and visited[nx]==0:
            visited[nx]=1;q.append(nx)
ans=[]
for i in range(n):
    if visited[i*2+1]==1 and visited[i*2]==0:ans+=[i+1]
print(' '.join(map(str,ans)))