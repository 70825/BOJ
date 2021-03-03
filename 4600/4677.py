import sys
sys.setrecursionlimit(100000)
dx,dy=[0,0,1,1,1,-1,-1,-1],[1,-1,0,1,-1,0,1,-1]
def DFS(x,y):
    for k in range(8):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='@' and S[nx][ny]==0:
            S[nx][ny]=t;DFS(nx,ny)
while 1:
    n,m=map(int,input().split())
    if n==m==0:break
    D=[input() for _ in range(n)]
    S=[[0]*m for _ in range(n)]
    t=1
    for i in range(n):
        for j in range(m):
            if D[i][j]=='@' and S[i][j]==0:S[i][j]=t;DFS(i,j);t+=1
    print(t-1)