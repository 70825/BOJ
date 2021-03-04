dx,dy=[0,0,1,1,1,-1,-1,-1],[1,-1,0,1,-1,0,1,-1]
n,m=map(int,input().split());t=1
D=[input() for _ in range(n)]
S=[[0]*m for _ in range(n)]
def dfs(x,y):
    for k in range(8):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='#' and S[nx][ny]==0:
            S[nx][ny]=t;dfs(nx,ny)
for i in range(n):
    for j in range(m):
        if D[i][j]=='#' and S[i][j]==0:
            S[i][j]=t;dfs(i,j);t+=1
print(t-1)