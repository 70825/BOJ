from collections import deque
n,m=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[0]*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
q=deque();t=1
def bfs():
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]==1 and S[nx][ny]==0:
                q.append((nx,ny));S[nx][ny]=t
for i in range(n):
    for j in range(m):
        if D[i][j]==1 and S[i][j]==0:
            q.append((i,j));S[i][j]=t;bfs();t+=1
K=[0]*t
for i in range(n):
    for j in range(m):
        if S[i][j]!=0:K[S[i][j]]+=1
K=sorted(K[1::],reverse=True)
print(t-1)
if t==1:print(0)
else:print(K[0])