from collections import deque
Max=10**6
for _ in range(int(input())):
    m,n=map(int,input().split())
    D=[list(map(str,[*input()])) for __ in range(n)]
    S=[[Max]*m for ___ in range(n)]
    q=deque();ans=Max
    dx,dy=[0,0,1,-1],[1,-1,0,0]
    for i in range(n):
        for j in range(m):
            if D[i][j]=='*':q.append((i,j));S[i][j]=0
            if D[i][j]=='@':ax=i;ay=j
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]=='.' and S[nx][ny]==Max:q.append((nx,ny));S[nx][ny]=S[x][y]+1
    q.append((ax,ay));S[ax][ay]=0
    while q:
        x,y=q.popleft()
        if (x==0 or x==n-1) and 0<=y<m:ans=min(ans,S[x][y])
        if 0<=x<n and (y==0 or y==m-1):ans=min(ans,S[x][y])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]=='.' and S[x][y]+1<S[nx][ny]:q.append((nx,ny));S[nx][ny]=S[x][y]+1
    print([ans+1,'IMPOSSIBLE'][ans==Max])