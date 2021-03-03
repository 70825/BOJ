from collections import deque

n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[0]*m for _ in range(n)]

q=deque([(0,0)])
S[0][0] = 1

dx,dy = [0,0,1,-1],[1,-1,0,0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny] == '1' and S[nx][ny]==0:
            S[nx][ny] = S[x][y] + 1
            q.append((nx,ny))

print(S[n-1][m-1])