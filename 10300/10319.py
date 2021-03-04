def edge(x,y,z=float('inf')):
    c[(x,y)]=z
    path[x].append(y)
    path[y].append(x)
def bfs():
    global level
    level=[-1]*nm
    level[S]=0
    q=deque([S])
    while q:
        x=q.popleft()
        for nx in path[x]:
            if c[(x,nx)]-f[(x,nx)]>0 and level[nx]==-1:
                level[nx]=level[x]+1;q.append(nx)
    return level[E]>0
def dfs(x,end,flow):
    if x==end:return flow
    while work[x]<len(path[x]):
        nx=path[x][work[x]]
        if c[(x,nx)]-f[(x,nx)]>0 and level[nx]==level[x]+1:
            df = dfs(nx,end,min(c[(x,nx)]-f[(x,nx)],flow))
            if df>0:
                f[(x,nx)]+=df
                f[(nx,x)]-=df
                return df
        work[x]+=1
    return 0
from collections import deque,defaultdict
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n=int(input())
    st,g,s=map(int,input().split());st-=1
    nm=n*(s+1)+2
    S=nm-2;E=S+1
    c=defaultdict(int)
    f=defaultdict(int)
    path=[[] for _ in range(nm)]
    edge(S,st*(s+1),g)
    for i in range(int(input())):
        x=int(input())-1
        edge(x*(s+1)+s,E,100)
    for i in range(int(input())):
        x,y,z,t=map(int,input().split())
        x-=1;y-=1
        for j in range(s-t+1):
            nx,ny=x*(s+1)+j,y*(s+1)+j+t
            edge(nx,ny,z)
    for i in range(n):
        for j in range(s):
            nx,ny=i*(s+1)+j,i*(s+1)+j+1
            edge(nx,ny,100)
    res=0
    level=[-1]*nm
    while bfs():
        work=[0]*nm
        while 1:
            flow=dfs(S,E,float('inf'))
            if flow==0:break
            res+=flow
    print(res)