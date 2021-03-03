def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if C[nx]==-1 or (not visited[C[nx]] and dfs(C[nx])):
            R[x]=nx
            C[nx]=x
            return 1
    return 0
r,c,n=map(int,input().split())
D=[[1]*c for _ in range(r)]
for i in range(n):
    x,y=map(int,input().split())
    D[x-1][y-1]=0
path=[[] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if D[i][j]==1:path[i].append(j)
R=[-1]*r
C=[-1]*c
res=0
for i in range(r):
    if R[i]==-1:
        visited=[0]*r
        if dfs(i): res+=1
print(res)