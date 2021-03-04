from collections import deque
n,m=map(int,input().split())
D=[list(map(int,[*input()])) for _ in range(n)]
S=[[[-1]*3 for _ in range(m)] for _ in range(n)]
q,dx,dy=deque(),[0,0,1,-1],[1,-1,0,0]
for i in range(3):
    a,b=map(int,input().split())
    q.append((a-1,b-1,i))
    S[a-1][b-1][i]=0
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0 and S[nx][ny][z]==-1:
            q.append((nx,ny,z));S[nx][ny][z]=S[x][y][z]+1
ans=10000;t=0
for i in range(n):
    for j in range(m):
        if min(S[i][j])!=-1:
            if ans>max(S[i][j]):ans=max(S[i][j]);t=1
            elif max(S[i][j])==ans:t+=1
if ans==10000:print(-1)
else:print(ans);print(t)