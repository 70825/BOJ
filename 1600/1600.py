from collections import deque
K=int(input())
m,n=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[[-1]*(K+1) for _ in range(m)] for __ in range(n)]
q=deque([(0,0,0)]);S[0][0][0]=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
ax,ay=[-2,-2,-1,-1,1,1,2,2],[1,-1,-2,2,-2,2,-1,1]
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0 and S[nx][ny][z]==-1:
            q.append((nx,ny,z));S[nx][ny][z]=S[x][y][z]+1
    for i in range(8):
        nx,ny=x+ax[i],y+ay[i]
        if z<K and 0<=nx<n and 0<=ny<m and D[nx][ny]==0 and S[nx][ny][z+1]==-1:
            q.append((nx,ny,z+1));S[nx][ny][z+1]=S[x][y][z]+1
ans=40000
for i in range(K+1):
    z=S[n-1][m-1][i]
    if z!=-1 and ans>z:ans=S[n-1][m-1][i]
print([ans,-1][ans==40000])