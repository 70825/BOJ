from collections import deque
q,dx,dy=deque(),[0,0,1,-1],[1,-1,0,0]
for __ in range(int(input())):
    m,n,k=map(int,input().split())
    D=[[0]*m for _ in range(n)]
    for i in range(k):
        y,x=map(int,input().split())
        D[x][y]=1
    ans=0
    for i in range(n):
        for j in range(m):
            if D[i][j]==1:
                q.append((i,j));D[i][j]=0;ans+=1
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m and D[nx][ny]==1:
                            q.append((nx,ny));D[nx][ny]=0
    print(ans)