from collections import deque
m,n,h=map(int,input().split())
D=[list(list(map(int,[*map(int,input().split())])) for _ in range(n)) for k in range(h)]
dx,dy,dz=[0,0,0,0,1,-1],[0,0,1,-1,0,0],[-1,1,0,0,0,0]
S=[[[-1]*m for _ in range(n)] for p in range(h)]
q=deque();ans=0;ANS=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if D[i][j][k]==1:
                q.append((i,j,k))
                S[i][j][k]=0
while q:
    x,y,z=q.popleft()
    for i in range(6):
        nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and S[nx][ny][nz]==-1 and D[nx][ny][nz]==0:
            q.append((nx,ny,nz))
            S[nx][ny][nz]=S[x][y][z]+1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if D[i][j][k]!=-1 and S[i][j][k]==-1:ans=-1
            ANS=max(ANS,S[i][j][k])
if ans==-1:print(-1)
else:print(ANS)