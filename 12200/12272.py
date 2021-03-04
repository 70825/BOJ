from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
Max=10000
for ___ in range(int(input())):
    n,m=map(int,input().split())
    a,b,ax,ay=map(int,input().split())
    D=[list(map(int,input().split())) for _ in range(n)]
    S=[[[Max,-1] for __ in range(m)] for _ in range(n)]
    q=deque([(a,b)]);S[a][b][0],S[a][b][1]=0,D[a][b]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!=-1:
                if S[nx][ny][0]>=S[x][y][0]+1 and S[nx][ny][1]<S[x][y][1]+D[nx][ny]:
                    q.append((nx,ny));S[nx][ny][0],S[nx][ny][1]=S[x][y][0]+1,S[x][y][1]+D[nx][ny]
    print('Case #{}:'.format(___+1),end=' ')
    print([S[ax][ay][1],'Mission Impossible.'][S[ax][ay][1]==-1])