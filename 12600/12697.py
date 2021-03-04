from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
tr=deque()
for ___ in range(int(input())):
    n,m=map(int,input().split())
    D=[list(map(str,[*input()])) for _ in range(n)]
    S=[[-1]*m for _ in range(n)]
    q=deque()
    for i in range(n):
        for j in range(m):
            if D[i][j]=='O':q.append((i,j,deque()));S[i][j]=0
            elif D[i][j]=='X':ax,ay=i,j
    while q:
        x,y,portal=q.popleft()
        for i in range(4):
            nx,ny,t=x+dx[i],y+dy[i],0
            while 1:
                if 0<=nx<n and 0<=ny<m and D[nx][ny]=='#':
                    a,b,t=nx-dx[i],ny-dy[i],1
                    if S[a][b]==-1:portal.append((a,b))
                elif nx<0 or nx>=n or ny<0 or ny>=m:
                    a,b,t=nx-dx[i],ny-dy[i],1
                    if S[a][b]==-1:portal.append((a,b))
                if t==1:break
                nx+=dx[i];ny+=dy[i]
        for i in range(4):
            nx,ny,Port=x+dx[i],y+dy[i],portal+tr
            if (0<=nx<n and 0<=ny<m and D[nx][ny]=='#') or nx<0 or nx>=n or ny<0 or ny>=m:
                while Port:
                    a,b=Port.popleft()
                    if S[a][b]==-1:q.append((a,b,deque()));S[a][b]=S[x][y]+1
            elif 0<=nx<n and 0<=ny<m and D[nx][ny]!='#' and S[nx][ny]==-1:
                q.append((nx,ny,Port));S[nx][ny]=S[x][y]+1
    print('Case #{}:'.format(___+1),end=' ')
    print([S[ax][ay],'THE CAKE IS A LIE'][S[ax][ay]==-1])