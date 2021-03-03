from collections import deque
n,m=map(int,input().split());Max=10**6
D=[list(map(str,[*input()])) for _ in range(n)]
S=[[Max]*m for _ in range(n)]
q=deque();ans=Max
dx,dy=[0,0,-1,1],[-1,1,0,0]
for i in range(n):
    for j in range(m):
        if D[i][j]=='J':ax=i;ay=j
        elif D[i][j]=='F':q.append((i,j));S[i][j]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='.' and S[nx][ny]==Max:q.append((nx,ny));S[nx][ny]=S[x][y]+1
q.append((ax,ay));S[ax][ay]=0
while q:
    x,y=q.popleft()
    if (x==0 or x==n-1) and 0<=y<m and D[x][y] in '.J':ans=min(ans,S[x][y])
    elif (y==0 or y==m-1) and 0<=x<n and D[x][y] in '.J':ans=min(ans,S[x][y])
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]=='.' and S[x][y]+1<S[nx][ny]:
            q.append((nx,ny));S[nx][ny]=S[x][y]+1
if ans==10**6:print('IMPOSSIBLE')
else:print(ans+1)