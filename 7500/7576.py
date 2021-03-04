from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
m,n=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
a=[[-1]*m for _ in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if D[i][j]==1:
            a[i][j]=0
            q.append((i,j))
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if D[nx][ny]==0 and a[nx][ny]==-1:
                q.append((nx,ny))
                a[nx][ny]=a[x][y]+1
ans=max([max(row) for row in a])
for i in range(n):
    for j in range(m):
        if D[i][j]==0 and a[i][j]==-1:
            ans=-1
print(ans)