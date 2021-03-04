def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if odd[nx]==-1 or (not visited[odd[nx]] and dfs(odd[nx])):
            even[x]=nx
            odd[nx]=x
            return 1
    return 0
n,m=map(int,input().split())
D=[input() for _ in range(n)]
Num=[[-1]*m for _ in range(n)]
res=0
a,b=0,0
A,B=[],[]
for i in range(n*m):
    x,y=i//m,i%m
    if D[x][y]=='.':
        if (x+y)%2==0:
            Num[x][y]=a;a+=1
            A.append([x,y])
        else:
            Num[x][y]=b;b+=1
            B.append([x,y])
        res+=1
path=[[] for _ in range(a)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(a):
    x,y=A[i]
    for j in range(4):
        nx,ny=x+dx[j],y+dy[j]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='.':
            path[i].append(Num[nx][ny])
even=[-1]*a
odd=[-1]*b
for i in range(a):
    if even[i]==-1:
        visited=[0]*a
        if dfs(i):res-=1
print(res)