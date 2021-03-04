from collections import deque
n,m=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if D[i][j]==0:S[i][j]=0
        if D[i][j]==2:q=deque([(i,j)]);S[i][j]=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if D[nx][ny]==1 and S[nx][ny]==-1:
                q.append((nx,ny));S[nx][ny]=S[x][y]+1
for i in range(n):print(*S[i])