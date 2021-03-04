def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            P[x]=nx
            B[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
path=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    path[a].append(b)
P=[-1]*n
B=[-1]*n
res=0
for i in range(n):
    if P[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
print(['NO','YES'][res==n])