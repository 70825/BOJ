import sys
from collections import deque
n,m=map(int,input().split())
D=[[*input()] for _ in range(n)]
C=[[[-1]*m for _ in range(n)] for __ in range(1<<6)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if D[i][j]=='0':q=deque([[0,i,j]]);C[0][i][j]=0
while q:
    key,x,y=q.popleft()
    if D[x][y]=='1':print(C[key][x][y]);sys.exit(0)
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[x][y]!='#':
            if D[nx][ny] in 'abcdef':
                nkey = key | 1<<(ord(D[nx][ny])-97)
                if C[nkey][nx][ny]==-1:C[nkey][nx][ny]=C[key][x][y]+1;q.append([nkey,nx,ny])
            if D[nx][ny] in 'ABCDEF' and key & 1<<(ord(D[nx][ny])-65) and C[key][nx][ny]==-1:
                C[key][nx][ny]=C[key][x][y]+1;q.append([key,nx,ny])
            if D[nx][ny] in '.01' and C[key][nx][ny]==-1:
                C[key][nx][ny]=C[key][x][y]+1;q.append([key,nx,ny])
print(-1)