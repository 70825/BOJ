def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if H[nx]==-1 or (not visited[H[nx]] and dfs(H[nx])):
            R[x]=nx
            H[nx]=x
            return 1
    return 0
def length(x1,y1,x2,y2):return ((x1-x2)**2+(y1-y2)**2)**0.5
input=__import__('sys').stdin.readline
n,m,s,v=map(int,input().split())
rat=[[*map(float,input().split())] for _ in range(n)]
house=[[*map(float,input().split())] for _ in range(m)]
path=[[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        x1,y1=rat[i];x2,y2=house[j]
        if s*v>=length(x1,y1,x2,y2):
            path[i].append(j)
R=[-1]*n
H=[-1]*m
res=0
for i in range(n):
    if R[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
print(n-res)