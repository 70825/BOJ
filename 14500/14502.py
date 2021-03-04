import copy
import itertools
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
input=__import__('sys').stdin.readline

def FloodFill(t):
    for i in range(n):
        for j in range(m):
            if S[i][j]==2:
                q=deque([(i,j)]);bfs(q)
    for i in range(n):
        for j in range(m):
            if S[i][j]==0:t+=1
    return t
def bfs(q):
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and S[nx][ny]==0:
                S[nx][ny]=2;q.append((nx,ny))

n,m=map(int,input().split())
ans=0
D=[[*map(int,input().split())] for _ in range(n)]
K=[]
for i in range(n):
    for j in range(m):
        if D[i][j]==0:
            K.append([i,j])
for a,b,c in itertools.combinations(K,3):
    S=copy.deepcopy(D)
    S[a[0]][a[1]],S[b[0]][b[1]],S[c[0]][c[1]]=1,1,1
    ans=max(ans,FloodFill(0))
print(ans)