from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[0]*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
ans=0
for i in range(n):
    for j in range(m):
        if D[i][j]=='#' and S[i][j]==0:
            q=deque([(i,j)]);S[i][j]=1;ans+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<m and D[nx][ny]=='#' and S[nx][ny]==0:
                        q.append((nx,ny));S[nx][ny]=1
print(ans)