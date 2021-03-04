from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
c=[[0]*n for _ in range(n)]
f=[[0]*n for _ in range(n)]
path=[[] for _ in range(n)]
S=0;E=n-1
for i in range(m):
    x,y,z=map(int,input().split())
    x-=1;y-=1
    c[x][y]+=z
    c[y][x]+=z
    path[x].append(y)
    path[y].append(x)
res=0
while 1:
    q=deque([S])
    prev=[-1]*n
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[x][nx]-f[x][nx]>0 and prev[nx]==-1:
                prev[nx]=x
                q.append(nx)
    if prev[E]==-1:break
    x=E
    while x!=S:
        nx=prev[x]
        f[nx][x]+=1
        f[x][nx]-=1
        x=nx
    res+=1
print(res)