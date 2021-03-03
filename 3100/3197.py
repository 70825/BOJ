def find(x):
    if(p[x]==x):return x
    p[x] = find(p[x])
    return p[x]
def merge(x,y):
    x,y=find(x),find(y)
    p[y]=x
input=__import__('sys').stdin.readline
import sys
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[[*input()] for _ in range(n)]
check=[[-1]*m for _ in range(n)]
q=deque()
pq=deque()
bird=[]
z=0
for i in range(n):
    for j in range(m):
        if D[i][j]!='X' and check[i][j]==-1:check[i][j]=z;z+=1;pq.append([i,j,0])
        if D[i][j]=='L':bird.append([i,j])
p=[i for i in range(z)]
x1,y1=bird[0]
x2,y2=bird[1]
while 1:
    while pq:
        x,y,t=pq.popleft()
        q.append([x,y,t])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and check[nx][ny]!=-1 and find(p[check[x][y]])!=find(p[check[nx][ny]]):
                merge(check[x][y], check[nx][ny])
                if find(p[check[x1][y1]]) == find(p[check[x2][y2]]):print(t);sys.exit(0)
    while q:
        x,y,t=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and check[nx][ny]==-1:
                check[nx][ny]=check[x][y];pq.append([nx,ny,t+1])