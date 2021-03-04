from collections import deque
while 1:
    N,M=map(int,input().split())
    if N==M==0:break
    D=[[*input()] for _ in range(M)]
    q=deque()
    for i in range(M):
        for j in range(N):
            if D[i][j]=='S':q.append((i,j))
    dx,dy=[0,0,1,-1],[1,-1,0,0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N and D[nx][ny]=='T':
                q.append((nx,ny))
                D[nx][ny]='S'
    for i in range(M):print(''.join(map(str,D[i])))