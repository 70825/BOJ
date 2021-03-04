m,n=map(int,input().split())
k=int(input())
if k>m*n:print(0);exit()
D=[[0]*m for _ in range(n)]
dx,dy=[-1,0,1,0],[0,1,0,-1]
q=[(n-1,0,0)]
D[n-1][0]=1
while q:
    x,y,z=q.pop()
    if D[x][y]==k:print(y+1,n-x);exit()
    nx,ny=x+dx[z],y+dy[z]
    if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
        q.append((nx,ny,z));D[nx][ny]=D[x][y]+1
    else:
        z=(z+1)%4
        nx,ny=x+dx[z],y+dy[z]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
            q.append((nx,ny,z));D[nx][ny]=D[x][y]+1