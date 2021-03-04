from collections import deque
n,m=map(int,input().split())
D=[list(map(int,[*input()])) for _ in range(n)]
q=deque();z=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(m):
    if D[0][i]==0:
        q.append((0,i));D[0][i]=1
        while q:
            x,y=q.popleft()
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
                    q.append((nx,ny));D[nx][ny]=1
                    if nx==n-1:z+=1
print(['NO','YES'][z>0])