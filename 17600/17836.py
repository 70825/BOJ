from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m,t=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
check=[[float('inf')]*m for _ in range(n)]
q=deque([[0,0]]);check[0][0]=0
ans=float('inf')
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]!=1 and check[nx][ny]==float('inf'):
            check[nx][ny]=check[x][y]+1
            q.append([nx,ny])
            if D[nx][ny]==2:ans=check[nx][ny]+n+m-2-nx-ny
ans=min(check[n-1][m-1],ans)
print([ans,'Fail'][ans>t])