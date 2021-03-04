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
n,k=map(int,input().split())
check=[[-1]*(n+1) for _ in range(n+1)]
p=[-1]*k
q=deque()
pq=deque()
conquer=1
for i in range(k):
    x,y=map(int,input().split())
    check[x][y]=i;p[i]=i
    q.append([x,y,0])
while 1:
    while q:
        x,y,t=q.popleft()
        pq.append([x,y,t])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 1<=nx<n+1 and 1<=ny<n+1 and check[nx][ny]!=-1 and find(p[check[x][y]])!=find(p[check[nx][ny]]):
                merge(check[x][y],check[nx][ny]);conquer+=1
                if conquer==k:print(t);sys.exit(0)
    while pq:
        x,y,t=pq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 1<=nx<n+1 and 1<=ny<n+1 and check[nx][ny]==-1:
                check[nx][ny]=check[x][y];q.append([nx,ny,t+1])