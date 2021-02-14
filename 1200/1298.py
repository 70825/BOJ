def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if N[nx]==-1 or (not visited[N[nx]] and dfs(N[nx])):
            P[x]=nx
            N[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    path[a].append(b)
P=[-1]*n
N=[-1]*n
res=0
for i in range(n):
    if P[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
print(res)