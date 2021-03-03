def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if col[nx]==-1 or (not visited[col[nx]] and dfs(col[nx])):
            row[x]=nx
            col[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
R=[[-1]*m for _ in range(n)]
C=[[-1]*m for _ in range(n)]
r,c=0,0
now1,now2=0,0
for i in range(n):
    if now1!=0:r+=1;now1=0
    for j in range(m):
        if D[i][j]==0:R[i][j]=r;now1+=1
        if D[i][j]==2 and now1!=0:r+=1;now1=0
for j in range(m):
    if now2!=0:c+=1;now2=0
    for i in range(n):
        if D[i][j]==0:C[i][j]=c;now2+=1
        if D[i][j]==2 and now2!=0:c+=1;now2=0
r+=1;c+=1
path=[[] for _ in range(r)]
for i in range(n):
    for j in range(m):
        if R[i][j]>=0 and C[i][j]>=0:
            path[R[i][j]].append(C[i][j])
row=[-1]*r
col=[-1]*c
res=0
for i in range(r):
    if row[i]==-1:
        visited=[0]*r
        if dfs(i):res+=1
print(res)