def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if left[nx]==-1 or (not visited[left[nx]] and dfs(left[nx])):
            right[x]=nx
            left[nx]=x
            return 1
    return 0
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
R=[[-1]*n for _ in range(n)]
L=[[-1]*n for _ in range(n)]
r,l=-1,-1
for i in range(n):
    r+=1
    x,y=0,i
    for j in range(n-1-i,-1,-1):
        if D[x][y]==1:R[x][y]=r
        x+=1;y+=1
for i in range(1,n):
    r+=1
    x,y=i,0
    for j in range(n-i-1,-1,-1):
        if D[x][y]==1:R[x][y]=r
        x+=1;y+=1
for i in range(n):
    l+=1
    x,y=0,i
    for j in range(n):
        if D[x][y]==1:L[x][y]=l
        x+=1;y-=1
for i in range(1,n):
    l+=1
    x,y=i,n-1
    for j in range(n-1-i,-1,-1):
        if D[x][y]==1:L[x][y]=l
        x+=1;y-=1
r+=1;l+=1
path=[[] for _ in range(r)]
for i in range(n):
    for j in range(n):
        if R[i][j]>=0 and L[i][j]>=0:
            path[R[i][j]].append(L[i][j])
right=[-1]*r
left=[-1]*l
res=0
for i in range(r):
    if right[i]==-1:
        visited=[0]*r
        if dfs(i):res+=1
print(res)