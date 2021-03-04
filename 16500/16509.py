from collections import deque
r,c=map(int,input().split())
a,b=map(int,input().split())
D=[[-1]*9 for _ in range(10)];D[r][c]=0
q=deque();q.append((r,c))
dx=[[0,-1,-1],[0,-1,-1],[-1,-1,-1],[-1,-1,-1],[0,1,1],[0,1,1],[1,1,1],[1,1,1]]
dy=[[-1,-1,-1],[1,1,1],[0,-1,-1],[0,1,1],[-1,-1,-1],[1,1,1],[0,-1,-1],[0,1,1]]
while q:
    x,y=q.popleft()
    for i in range(8):
        err=0
        nx,ny=x,y
        for j in range(2):
            nx+=dx[i][j];ny+=dy[i][j]
            if nx==a and ny==b:err=1
        nx,ny=x+sum(dx[i]),y+sum(dy[i])
        if err==0 and 0<=nx<10 and 0<=ny<9 and D[nx][ny]==-1:
            D[nx][ny]=D[x][y]+1
            q.append((nx,ny))
print(D[a][b])