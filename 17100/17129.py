from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[-1]*m for _ in range(n)]
dx,dy=[1,-1,0,0],[0,0,1,-1]
q=deque()
for i in range(n):
    for j in range(m):
        if D[i][j]=='2':q.append((i,j));S[i][j]=0
while q:
    x,y=q.popleft()
    if D[x][y] in '345':print('TAK');print(S[x][y]);exit()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]!='1' and S[nx][ny]==-1:
            S[nx][ny]=S[x][y]+1
            q.append((nx,ny))
print('NIE')