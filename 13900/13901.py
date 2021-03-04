from collections import deque
n,m=map(int,input().split())
D=[[0]*m for _ in range(n)]
for i in range(int(input())):
    a,b=map(int,input().split())
    D[a][b]=1
a,b=map(int,input().split())
q=deque([(a,b,0)]);D[a][b]=1
P=[*map(int,input().split())]
while q:
    x,y,z=q.popleft()
    ans=z;t=0
    while 1:
        if P[ans]==1:nx,ny=x-1,y
        elif P[ans]==2:nx,ny=x+1,y
        elif P[ans]==3:nx,ny=x,y-1
        else:nx,ny=x,y+1
        if 0<=nx<n and 0<=ny<m and D[nx][ny]==0:
            q.append((nx,ny,ans));D[nx][ny]=1;break
        else:ans+=1;ans%=4;t+=1
        if t==4:break
    if t==4:print(x,y);break