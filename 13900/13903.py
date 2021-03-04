from collections import deque
n,m=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(n)]
k=int(input())
S=[[-1]*m for _ in range(n)]
q=deque();ans,dx,dy=10**6,[0]*k,[0]*k
for i in range(m):
    if D[0][i]==1:q.append((0,i));S[0][i]=0
for i in range(k):
    x,y=map(int,input().split())
    dx[i],dy[i]=x,y
while q:
    x,y=q.popleft()
    for i in range(k):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==1 and S[nx][ny]==-1:
            q.append((nx,ny));S[nx][ny]=S[x][y]+1
for i in range(m):
    if D[n-1][i]==1 and S[n-1][i]!=-1:ans=min(ans,S[n-1][i])
print([ans,-1][ans==10**6])