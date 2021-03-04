from collections import deque
R,C=map(int,input().split())
pixel=[list(map(str,[*input()])) for _ in range(R)]
Y,X,K=map(int,input().split())
q=deque();q.append((Y,X))
z=pixel[Y][X];pixel[Y][X]=K
dx,dy=[1,-1,0,0],[0,0,-1,1]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if pixel[nx][ny]==z and pixel[nx][ny]!=K:
                q.append((nx,ny))
                pixel[nx][ny]=K
for i in range(R):print(''.join(map(str,pixel[i])))