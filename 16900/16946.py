def bfs(a,b):
    ans=1;S[a][b]=t;q=deque([(a,b)])
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]=='0' and S[nx][ny]==-1:
                ans+=1;S[nx][ny]=t;q.append((nx,ny))
    return ans
def Sum(x,y):
    G=[]
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='0':
            G.append(S[nx][ny])
    ans=sum([P[k] for k in [*set(G)]])+1
    return ans%10
from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[-1]*m for _ in range(n)]
K=[[0]*m for _ in range(n)]
P=[];t=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if D[i][j]=='0' and S[i][j]==-1:
            P.append(bfs(i,j));t+=1
for i in range(n):
    for j in range(m):
        if D[i][j]=='1':
            K[i][j]=Sum(i,j)
for i in range(n):
    print(''.join(map(str,K[i])))