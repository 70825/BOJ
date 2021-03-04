def edge(x,y,z):
    c[x][y]+=z
    c[y][x]+=z
    path[x].append(y)
    path[y].append(x)
def convert(x):return ord(x)-65 if x==x.upper() else ord(x)-71
def bfs():
    global level
    level=[-1]*52
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
c=[[0]*52 for _ in range(52)]
f=[[0]*52 for _ in range(52)]
path=[[] for _ in range(52)]
level=[-1]*52
for _ in range(int(input())):
    x,y,z=input().strip().split()
    edge(convert(x),convert(y),int(z))
S=convert('A')
E=convert('Z')
res=0
while bfs():
    work=[0]*52
    while 1:
        flow=dfs(S,E,float('inf'))
        if flow==0:break
        res+=flow
print(res)