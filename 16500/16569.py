from collections import deque
dx,dy,Max=[0,0,1,-1],[1,-1,0,0],500000
n,m,v=map(int,input().split())
ax,ay=map(int,input().split())
q=deque([(ax-1,ay-1)]);Fq=deque()
D=[list(map(int,input().split())) for _ in range(n)]
S=[[-1]*m for _ in range(n)];S[ax-1][ay-1]=0
FS=[[Max]*m for _ in range(n)]
h,t=D[ax-1][ay-1],0
for _ in range(v):
    x,y,z=map(int,input().split())
    Fq.append((x-1,y-1,z));FS[x-1][y-1]=z;S[x-1][y-1]=-2
while Fq:
    x,y,z=Fq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and FS[nx][ny]>z+1:
            Fq.append((nx,ny,z+1));FS[nx][ny]=z+1
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and S[nx][ny]==-1 and FS[nx][ny]>S[x][y]+1:
            q.append((nx,ny));S[nx][ny]=S[x][y]+1
            if D[nx][ny]>h:h=D[nx][ny];t=S[nx][ny]
print(h,t)