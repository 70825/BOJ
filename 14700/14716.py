def FloodFill():
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for k in range(8):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]==1:
                q.append((nx,ny));D[nx][ny]=0

from collections import deque
n,m=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
ans=0
dx,dy=[0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]
for i in range(n):
    for j in range(m):
        if D[i][j]==1:FloodFill();ans+=1   
print(ans)