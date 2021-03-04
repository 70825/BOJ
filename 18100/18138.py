def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            A[x]=nx
            B[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
path=[[] for _ in range(n)]
shirt=[0]*n
collar=[0]*m
for i in range(n):
    shirt[i]=int(input())
for i in range(m):
    collar[i]=int(input())
    for j in range(n):
        w=shirt[j]
        if 0.5*w<=collar[i]<=0.75*w or w<=collar[i]<=1.25*w:
            path[j].append(i)
res=0
A=[-1]*n
B=[-1]*m
for i in range(n):
    if A[i]==-1:
        visited=[0]*n
        if dfs(i): res+=1
print(res)