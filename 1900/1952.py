n,m=map(int,input().split())
D=[[0]*m for _ in range(n)]
D[0][0]=1;q=[(0,0,0)];e=0
dx,dy=[0,1,0,-1],[1,0,-1,0]
while q:
    x,y,z=q.pop()
    nx,ny=x+dx[z],y+dy[z]
    if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
        D[nx][ny]=1;q.append((nx,ny,z))
    else:
        z=(z+1)%4
        nx,ny=x+dx[z],y+dy[z]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
            q.append((nx,ny,z));e+=1;D[nx][ny]=1
print(e)