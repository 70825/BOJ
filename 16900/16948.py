from collections import deque
n=int(input())
sx,sy,ex,ey=map(int,input().split())
S=[[0]*n for _ in range(n)]
dx,dy=[-2,-2,0,0,2,2],[-1,1,-2,2,-1,1]
q=deque([(sx,sy)]);S[sx][sy]=1
while q:
    x,y=q.popleft()
    for i in range(6):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and S[nx][ny]==0:
            S[nx][ny]=S[x][y]+1;q+=[(nx,ny)]
print(S[ex][ey]-1)