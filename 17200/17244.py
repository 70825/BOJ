def bfs(A,B):
    sx,sy=A;ex,ey=B
    S=[[-1]*m for _ in range(n)]
    q=deque([[sx,sy]])
    S[sx][sy]=0
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='#' and S[nx][ny]==-1:
                S[nx][ny]=S[x][y]+1;q.append([nx,ny])
    return S[ex][ey]
from collections import deque
from itertools import permutations as pm
input=__import__('sys').stdin.readline
dx,dy=[0,0,1,-1],[1,-1,0,0]
m,n=map(int,input().split())
D=[input() for _ in range(n)]
ob=[]
res=float('inf')
for i in range(n):
    for j in range(m):
        if D[i][j]=='X':ob+=[[i,j]]
        if D[i][j]=='S':S=[i,j]
        if D[i][j]=='E':E=[i,j]
if len(ob)==0:print(bfs(S,E));exit()
for T in pm(ob,len(ob)):
    ans=0
    ans+=bfs(S,T[0])
    for i in range(len(T)-1):
        ans+=bfs(T[i],T[i+1])
    ans+=bfs(T[-1],E)
    res=min(ans,res)
print(res)