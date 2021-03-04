def edge(x,y,z=float('inf')):
    c[x][y]+=z
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
n=int(input())
nm=n+2
S=nm-2;E=S+1
c=[[0]*nm for _ in range(nm)]
f=[[0]*nm for _ in range(nm)]
path=[[] for _ in range(nm)]
team=[*map(int,input().split())]
for i in range(n):
    if team[i]==1:edge(S,i)
    if team[i]==2:edge(i,E)
score=[[*map(int,input().split())] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if score[i][j]>0:
            c[i][j]=score[i][j];path[i].append(j)
res=0
level=[-1]*nm
while bfs():
    work=[0]*nm
    while 1:
        flow=dfs(S,E,float('inf'))
        if flow==0:break
        res+=flow
visited=[0]*nm
q=deque([S])
while q:
    x=q.popleft()
    for nx in path[x]:
        if c[x][nx]-f[x][nx]>0 and visited[nx]==0:
            visited[nx]=1;q.append(nx)
A,B=[],[]
for i in range(n):
    if visited[i]==1:A.append(i+1)
    else:B.append(i+1)
print(res)
print(' '.join(map(str,A)))
print(' '.join(map(str,B)))