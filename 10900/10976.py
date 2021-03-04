def edge(x,y,z):
    c[x][y]=z
    path[x].append(y)
    path[y].append(x)
from collections import deque
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,m=map(int,input().split())
    S=0;E=n-1
    c=[[0]*n for _ in range(n)]
    f=[[0]*n for _ in range(n)]
    path=[[] for _ in range(n)]
    for i in range(m):
        x,y=map(int,input().split())
        x-=1;y-=1
        if x==0:edge(x,y,1)
        elif y==n-1:edge(x,y,1)
        else:edge(x,y,10**10)
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