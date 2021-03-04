def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            A[x]=nx
            B[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    a-=1;b-=1
    path[a].append(b)
A=[-1]*n
B=[-1]*m
res=0
for i in range(n):
    if A[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
print(n+m-res)