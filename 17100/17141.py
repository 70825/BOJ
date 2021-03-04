from collections import deque
import copy
import itertools
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
K=[[0]*n for _ in range(n)]
Virus_Area=[]
ans=float('inf')
Area=n*n
for i in range(n):
    for j in range(n):
        if D[i][j]==2:Virus_Area.append((i,j))
        if D[i][j]==1:K[i][j]=-1;Area-=1
for Virus in itertools.combinations(Virus_Area,m):
    Map=copy.deepcopy(K)
    z=copy.deepcopy(Area)
    S=[[-1]*n for _ in range(n)]
    q, time=deque(), 0
    for x,y in Virus:
        Map[x][y]=1;S[x][y]=0;q.append((x,y));z-=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and Map[nx][ny]==0 and S[nx][ny]==-1:
                S[nx][ny]=S[x][y]+1;q.append((nx,ny));time=max(time,S[nx][ny]);z-=1
    if z==0:ans=min(ans,time)
print([ans,-1][ans==float('inf')])