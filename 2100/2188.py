def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if room[nx]==-1 or (not visited[room[nx]] and dfs(room[nx])):
            cow[x]=nx;room[nx]=x;return 1
    return 0
n,m=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(n):
    a,*b=map(int,input().split())
    for j in b: path[i].append(j-1)
res=0
cow=[-1]*n
room=[-1]*m
for i in range(n):
    if cow[i]==-1:
        visited=[0]*n
        if dfs(i): res+=1
print(res)