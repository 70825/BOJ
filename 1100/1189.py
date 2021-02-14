def go(x,y,check):
    global ans
    if x==0 and y==m-1:
        if check[x][y]==k:ans+=1
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]!='T' and C[nx][ny]==-1:
            C[nx][ny]=C[x][y]+1;go(nx,ny,C);C[nx][ny]=-1
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m,k=map(int,input().split())
D=[[*input()] for _ in range(n)]
C=[[-1]*m for _ in range(n)]
ans=0;C[n-1][0]=1
go(n-1,0,C)
print(ans)