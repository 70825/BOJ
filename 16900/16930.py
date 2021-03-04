from collections import deque
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[input().strip() for _ in range(n)]
sx,sy,ex,ey=map(int,input().split())
sx-=1;sy-=1;ex-=1;ey-=1
S=[[float('inf')]*m for _ in range(n)]
q=deque([(sx,sy)]);S[sx][sy]=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i];nk=1
        while nk<=k and 0<=nx<n and 0<=ny<m and D[nx][ny]!='#' and S[nx][ny]>S[x][y]:
            if S[nx][ny]==float('inf'):
                q.append((nx,ny));S[nx][ny]=S[x][y]+1
            nx+=dx[i];ny+=dy[i];nk+=1
print([S[ex][ey],-1][S[ex][ey]==float('inf')])