from collections import deque
for _ in range(int(input())):
    l=int(input())
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    D=[[-1]*l for p in range(l)];D[a][b]=0
    q=deque();q.append((a,b))
    dx,dy=[-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<l and 0<=ny<l and D[nx][ny]==-1:
                D[nx][ny]=D[x][y]+1
                q.append((nx,ny))
    print(D[c][d])