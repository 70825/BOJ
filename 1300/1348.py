def dfs(x,t):
    visited[x]=1
    for nt,nx in path[x]:
        if nt>t:break
        if P[nx]==-1 or (not visited[P[nx]] and dfs(P[nx],t)):
            C[x]=nx;P[nx]=x;Z[x]=nt
            return 1
    return 0
def bfs(A):
    global r
    q=deque([[A[0],A[1],0]])
    visited=[[-1]*m for _ in range(n)]
    visited[A[0]][A[1]]=0
    while q:
        x,y,t=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='X' and visited[nx][ny]==-1:
                visited[nx][ny]=t+1;q.append([nx,ny,t+1]);r=max(t+1,r)
                if D[nx][ny]=='P':path[i].append([t+1,Num[nx][ny]])
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[input() for _ in range(n)]
Num=[[-1]*m for _ in range(n)];num=0
Car=[]
for i in range(n):
    for j in range(m):
        if D[i][j]=='C':Car.append([i,j])
        if D[i][j]=='P':Num[i][j]=num;num+=1
if len(Car)==0:print(0);exit(0)
if len(Car)>num:print(-1);exit(0)
path=[[] for _ in range(len(Car))]
l,r=0,0
for i in range(len(Car)):
    bfs(Car[i])
    path[i]=sorted(path[i])
res=-1
while l<=r:
    m=(l+r)//2
    C=[-1]*len(Car)
    P=[-1]*num
    Z=[-1]*len(Car)
    ans=0
    for i in range(len(Car)):
        if C[i]==-1:
            visited=[0]*len(Car)
            if dfs(i,m):ans+=1
    if ans==len(Car):
        res=max(Z)
        r=m-1
    else:l=m+1
print(res)