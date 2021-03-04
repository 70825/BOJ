from collections import deque
n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
v=[[0]*m for _ in range(n)]
dx,dy,q=[0,0,-1,1],[1,-1,0,0],deque()
for i in range(n):
    for j in range(m):
        if D[i][j]=='W':q.append((i,j));v[i][j]=1
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if D[nx][ny]=='.' and v[nx][ny]==0:q.append((nx,ny));v[nx][ny]=1
        else:
            while 1:
                if D[nx][ny]=='#':nx-=dx[i];ny-=dy[i];break
                elif D[nx][ny]=='.':break
                nx+=dx[i];ny+=dy[i]
            if v[nx][ny]==0:q.append((nx,ny));v[nx][ny]=1
for i in range(n):
    for j in range(m):
        if D[i][j]=='.' and v[i][j]==0:D[i][j]='P'
for i in range(n):print(''.join(map(str,D[i])))