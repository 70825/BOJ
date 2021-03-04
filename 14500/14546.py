from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
for __ in range(int(input())):
    m,n,sx,sy,ex,ey=map(int,input().split())
    D=[list(map(str,[*input()])) for _ in range(n)]
    S=[[0]*n for _ in range(m)]
    q=deque([(sx-1,sy-1)]);S[sx-1][sy-1]=1
    D=[*zip(*D[::-1])]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and D[nx][ny]==D[sx-1][sy-1] and S[nx][ny]==0:
                q.append((nx,ny));S[nx][ny]=S[x][y]+1
    print(['NO','YES'][S[ex-1][ey-1]!=0])