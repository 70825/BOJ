from collections import deque
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
S=[[-1]*m for _ in range(n)]
q=deque()
dx,dy=[0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]
for i in range(n):
    for j in range(m):
        if D[i][j]==1:q.append((i,j));S[i][j]=0
ans=0
while q:
    x,y=q.popleft()
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0 and S[nx][ny]==-1:
            S[nx][ny]=S[x][y]+1;ans=max(ans,S[nx][ny]);q.append((nx,ny))
print(ans)