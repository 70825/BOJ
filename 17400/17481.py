def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if W[nx]==-1 or (not visited[W[nx]] and dfs(W[nx])):
            P[x]=nx
            W[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
W={}
path=[[] for _ in range(n)]
for i in range(m): W[input()]=-1
for i in range(n):
    a,*b=input().split()
    for j in b:
        path[i].append(j)
P=[-1]*n
res=0
for i in range(n):
    if P[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
if res==n:print('YES')
else:print('NO');print(res)