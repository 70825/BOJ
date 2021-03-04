from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[0]*m for _ in range(n)]
ans=0;q=deque();t=1
dx,dy=[0,0,1,-1],[1,-1,0,0]
def A(x,y,t):
    global ans
    if D[x][y]=='N':nx,ny= x + dx[3], y + dy[3]
    elif D[x][y]=='S':nx,ny= x + dx[2], y + dy[2]
    elif D[x][y]=='E':nx,ny = x + dx[0], y + dy[0]
    else:nx, ny = x + dx[1], y + dy[1]
    if 0<=nx<n and 0<=ny<m:
        if S[nx][ny]==0:S[nx][ny]=t;A(nx,ny,t)
        elif S[nx][ny]==t:ans+=1;return
        else:return
for i in range(n):
    for j in range(m):
        if S[i][j]==0:S[i][j]=t;A(i,j,t);t+=1
print(ans)