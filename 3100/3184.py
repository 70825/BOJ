from collections import deque
n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
check=[[0]*m for _ in range(n)]
s,v=0,0;q=deque()
dx,dy=[0,0,-1,1],[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if D[i][j]!='#' and check[i][j]==0:
            sheep,wolf=0,0
            q.append((i,j));check[i][j]=1
            if D[i][j]=='v':wolf+=1
            elif D[i][j]=='o':sheep+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<m and D[nx][ny]!='#' and check[nx][ny]==0:
                        q.append((nx,ny));check[nx][ny]=1
                        if D[nx][ny]=='v':wolf+=1
                        elif D[nx][ny]=='o':sheep+=1
            if wolf >= sheep:v+=wolf
            else:s+=sheep
print(s,v)