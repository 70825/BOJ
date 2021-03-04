from collections import deque
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
C=[[[float('inf')]*4 for __ in range(m)] for _ in range(n)]
q=deque()
for i in range(m):q.append([0,i,0]);C[0][i][0]=D[0][i]
while q:
    x,y,z=q.popleft()
    for dx,dy,nz in [[1,-1,1],[1,0,2],[1,1,3]]:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and z!=nz and C[nx][ny][nz]>C[x][y][z]+D[nx][ny]:
            C[nx][ny][nz]=C[x][y][z]+D[nx][ny];q.append([nx,ny,nz])
print(min(C[n-1][i][j] for i in range(m) for j in range(4)))