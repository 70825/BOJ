from collections import deque
input= __import__('sys').stdin.readline
n,m=map(int,input().split())
D=[input().strip() for _ in range(n)]
dx,dy=[1,-1,0],[1,1,1]
q=deque()
S=[[-1]*m for _ in range(n)]
O=[]
for i in range(n):
    for j in range(m):
        if D[i][j]=='R':q.append((i,j));S[i][j]=0
while q:
    x,y=q.popleft()
    for i in range(3):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]!='#':
            if D[nx][ny]=='C':
                k=S[x][y]+1
                if k>S[nx][ny]:S[nx][ny]=k;q.append((nx,ny))
            elif D[nx][ny]=='.':
                k=S[x][y]
                if k>S[nx][ny]:S[nx][ny]=k;q.append((nx,ny))
            else:
                k=S[x][y]
                if k>S[nx][ny]:S[nx][ny]=k;q.append((nx,ny));O.append(S[nx][ny])
if len(O)==0:print(-1)
else:print(max(O))