from collections import deque
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[input().rstrip() for _ in range(n)]
dx,dy=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
for __ in range(int(input())):
    sx,sy,ex,ey=map(int,input().split())
    sx-=1;sy-=1;ex-=1;ey-=1
    S=[[float('INF')]*m for _ in range(n)];S[sx][sy]=0
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft();z=S[x][y]
        if x==ex and y==ey:print(S[ex][ey]);break
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if i==int(D[x][y]):
                    if S[nx][ny]>z:S[nx][ny]=z;q.appendleft((nx,ny))
                else:
                    if S[nx][ny]>z+1:S[nx][ny]=z+1;q.append((nx,ny))