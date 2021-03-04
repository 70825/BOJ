from collections import deque
m,n=map(int,input().split())
D=[input() for _ in range(n)]
S=[[float('INF')]*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
C=[]
for i in range(n):
    for j in range(m):
        if D[i][j]=='C':C.append((i,j))
sx,sy=C[0][0],C[0][1]
ex,ey=C[1][0],C[1][1]
q=deque([(sx,sy)])
S[sx][sy]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        while 1:
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='*' and S[nx][ny]>=S[x][y]+1:
                q.append((nx,ny));S[nx][ny]=S[x][y]+1
            else:break
            nx+=dx[i];ny+=dy[i]
print(S[ex][ey]-1)