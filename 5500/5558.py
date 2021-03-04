def bfs(a,b):
    K=[[-1]*m for _ in range(n)]
    q=deque([a])
    K[a[0]][a[1]]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='X' and K[nx][ny]==-1:
                K[nx][ny]=K[x][y]+1;q.append((nx,ny))
    return K[b[0]][b[1]]
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m,t=map(int,input().split())
D=[input() for _ in range(n)]
S=[0]*(t+1)
for i in range(n):
    for j in range(m):
        if D[i][j]=='S':S[0]=(i,j)
        if ord('1')<=ord(D[i][j])<=ord('9'):S[int(D[i][j])]=(i,j)
ans=sum(bfs(S[i],S[i+1]) for i in range(t))
print(ans)