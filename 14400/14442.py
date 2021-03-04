from collections import deque
n,m,k=map(int,input().split())
D=[list(map(int,[*input()])) for _ in range(n)]
S=[[[-1]*(k+1) for _ in range(m)] for __ in range(n)]
S[0][0][0]=1;q=deque([(0,0,0)])
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if D[nx][ny]==0 and S[nx][ny][z]==-1:
                q.append((nx,ny,z));S[nx][ny][z]=S[x][y][z]+1
            elif z<k and D[nx][ny]==1 and S[nx][ny][z+1]==-1:
                q.append((nx,ny,z+1));S[nx][ny][z+1]=S[x][y][z]+1
ans=10**6
for i in range(k+1):
    if S[n-1][m-1][i]!=-1:ans=min(ans,S[n-1][m-1][i])
print([ans,-1][ans==10**6])