from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
ans=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
def BFS(i,j):
    global ans
    S=[[-1]*m for _ in range(n)]
    q=deque([(i,j)]);S[i][j]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]=='L' and S[nx][ny]==-1:
                q.append((nx,ny));S[nx][ny]=S[x][y]+1;ans=max(ans,S[nx][ny])
for i in range(n):
    for j in range(m):
        if D[i][j]=='L':BFS(i,j)
print(ans)