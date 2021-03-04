from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
for __ in range(int(input())):
    n,m=map(int,input().split())
    D=[list(map(str,[*input()])) for _ in range(n)]
    S=[[-1]*m for _ in range(n)]
    Eq=deque();q=deque();ans=0
    for i in range(n):
        for j in range(m):
            if D[i][j]=='G':Eq.append((i,j))
            elif D[i][j]=='S':q.append((i,j));S[i][j]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny] in 'O0G' and S[nx][ny]==-1:
                q.append((nx,ny));S[nx][ny]=S[x][y]+1
    while Eq:
        x,y=Eq.popleft()
        if S[x][y]!=-1:
            if ans!=0:ans=min(ans,S[x][y])
            else:ans=S[x][y]
    print(['Shortest Path: {}'.format(ans),'No Exit'][ans==0])