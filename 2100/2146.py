def color():
    q=deque([(i,j)])
    Q.append((i,j))
    D[i][j]=col
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and D[nx][ny]==1:
                D[nx][ny]=col;q.append((nx,ny));Q.append((nx,ny))
def check():
    for i in range(n):
        for j in range(n):
            if D[i][j]!=0:
                for k in range(4):
                    x,y=i+dx[k],j+dy[k]
                    if 0<=x<n and 0<=y<n and D[x][y]!=0 and D[i][j]!=D[x][y]:
                        print(K[x][y]+K[i][j]);exit()
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
K=[[0]*n for _ in range(n)]
Q=deque()
q=deque()
col=2
for i in range(n):
    for j in range(n):
        if D[i][j]==1:color();col+=1
while Q:
    for i in range(len(Q)):
        x,y=Q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if D[nx][ny]==0:D[nx][ny]=D[x][y];K[nx][ny]=K[x][y]+1;q.append((nx,ny))
                elif D[x][y]!=D[nx][ny]:print(K[x][y]+K[nx][ny]);exit()
    check()
    if not Q:Q=q;q=deque()