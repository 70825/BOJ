def LAB(Virus):
    S=[[-1]*n for _ in range(n)]
    for x,y in Virus:S[x][y]=0
    q=deque([(x,y) for x,y in Virus])
    visit=Area;time=0
    while q:
        x,y=q.popleft()
        if visit==0:return time
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and D[nx][ny]!=1 and S[nx][ny]==-1:
                if D[nx][ny]==0:visit-=1;time=max(time,S[x][y]+1)
                S[nx][ny]=S[x][y]+1;q.append((nx,ny))
    return 10**5

from collections import deque
import itertools
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
Virus_Area=[]
Area=n*n
for i in range(n):
    for j in range(n):
        if D[i][j]==2:Virus_Area.append((i,j));Area-=1
        if D[i][j]==1:Area-=1
ans=(min(LAB(Virus) for Virus in itertools.combinations(Virus_Area,m)))
print([ans,-1][ans>10000])