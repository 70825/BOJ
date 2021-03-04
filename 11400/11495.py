def edge(x,y,z=float('inf')):
    c[x][y]=z
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
            if c[x][nx]-f[x][nx]>0 and level[nx]==-1:
                level[nx]=level[x]+1;q.append(nx)
    return level[E]>0
def dfs(x,end,flow):
    if x==end:return flow
    while work[x]<len(path[x]):
        nx=path[x][work[x]]
        if c[x][nx]-f[x][nx]>0 and level[nx]==level[x]+1:
            df = dfs(nx,end,min(c[x][nx]-f[x][nx],flow))
            if df>0:
                f[x][nx]+=df
                f[nx][x]-=df
                return df
        work[x]+=1
    return 0
from collections import deque
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,m=map(int,input().split())
    nm=n*m+2
    S=nm-2;E=S+1
    c=[[0]*nm for _ in range(nm)]
    f=[[0]*nm for _ in range(nm)]
    path=[[] for _ in range(nm)]
    D=[[*map(int,input().split())] for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            k=i*m+j
            if (i+j)%2==0:
                edge(S,k,D[i][j])
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx,ny=i+dx,j+dy;nk=nx*m+ny
                    if 0<=nx<n and 0<=ny<m:edge(k,nk)
            else:edge(k,E,D[i][j])
            ans+=D[i][j]
    res=0
    level=[-1]*nm
    while bfs():
        work=[0]*nm
        while 1:
            flow=dfs(S,E,float('inf'))
            if flow==0:break
            res+=flow
    print(ans-res)