def dfs(x):
    visited[x]=1
    for nx in path[x//(k+1)]:
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
        path[i]+=[j-1]
P=[-1]*(k+1)*n
W=[-1]*m
res=0
ans=0
now=0
t=1
for i in range(0,(k+1)*n,k+1):
    if P[i]==-1:
        visited=[0]*(k+1)*n
        if dfs(i): res+=1
while ans<=k:
    now=0
    for i in range(t,(k+1)*n,k+1):
        if P[i]==-1:
            visited=[0]*(k+1)*n
            if dfs(i): ans+=1;now+=1
    if now==0:break
    t+=1
if ans>k:print(res+k)
else:print(res+ans)