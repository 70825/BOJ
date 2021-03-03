def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            A[x]=nx
            B[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
D=[input() for _ in range(n)]
R=[[-1]*m for _ in range(n)]
C=[[-1]*m for _ in range(n)]
r=0;now=0
for i in range(n):
    if now==1:r+=1;now=0
    for j in range(m):
        if D[i][j]=='.' and now==1:r+=1;now=0
        if D[i][j]=='*':R[i][j]=r;now=1
c=0;now=0
for j in range(m):
    if now==1:c+=1;now=0
    for i in range(n):
        if D[i][j]=='.' and now==1:c+=1;now=0
        if D[i][j]=='*':C[i][j]=c;now=1
r+=1;c+=1
path=[[] for _ in range(r)]
for i in range(n):
    for j in range(m):
        if R[i][j]>=0 and C[i][j]>=0:
            path[R[i][j]].append(C[i][j])
A=[-1]*r
B=[-1]*c
res=0
for i in range(r):
    if A[i]==-1:
        visited=[0]*r
        if dfs(i):res+=1
print(res)