from collections import deque
n,m=map(int,input().split());Max=10**9
D=[list(map(int,input().split())) for _ in range(n)]
S=[[[Max]*2 for _ in range(m)] for __ in range(n)]
q=deque([(0,0,0)]);S[0][0][0]=D[0][0]
dx,dy=[1,-1,0,0],[0,0,-1,1]
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and S[nx][ny][z]>max(S[x][y][z],D[nx][ny]):
            q.append((nx,ny,z));S[nx][ny][z]=max(S[x][y][z],D[nx][ny])
        nx+=dx[i];ny+=dy[i]
        if z==0 and 0<=nx<n and 0<=ny<m and S[nx][ny][z+1]>max(S[x][y][z],D[nx][ny]):
            q.append((nx,ny,z+1));S[nx][ny][z+1]=max(S[x][y][z],D[nx][ny])
if S[n-1][m-1][0]==Max:print(S[n-1][m-1][1])
elif S[n-1][m-1][1]==Max:print(S[n-1][m-1][0])
else:print(min(S[n-1][m-1]))