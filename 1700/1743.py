def bfs():
    q = deque([(i,j)])
    t = 1
    D[i][j] = 0
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x + dx[w], y + dy[w]
            if 0 <= nx < n and 0 <= ny < m and D[nx][ny] == 1:
                q.append((nx, ny))
                t += 1
                D[nx][ny] = 0
    return t

from collections import deque
n,m,k=map(int,input().split())
D=[[0]*m for _ in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    D[a-1][b-1]=1
ans=0
dx,dy=[1,-1,0,0],[0,0,-1,1]
for i in range(n):
    for j in range(m):
        if D[i][j]==1:
            k=bfs()
            ans=max(ans,k)
print(ans)