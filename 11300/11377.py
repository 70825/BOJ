def dfs(x):
    visited[x]=1
    for nx in path[x//2]:
        if W[nx]==-1 or (not visited[W[nx]] and dfs(W[nx])):
            P[x]=nx
            W[nx]=x
            return 1
    return 0
n,m,k=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(n):
    a,*b=map(int,input().split())
    for j in b:
        path[i].append(j-1)
P=[-1]*2*n
W=[-1]*m
res=0
ans=0
for i in range(0,2*n,2):
    if P[i]==-1:
        visited=[0]*2*n
        if dfs(i): res+=1
for i in range(1,2*n,2):
    if ans==k:break
    if P[i]==-1:
        visited=[0]*2*n
        if dfs(i):ans+=1
print(res+ans)