from collections import deque
input=__import__('sys').stdin.readline
MIS=lambda:map(int,input().split())
def bfs():
    global ans,z
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and K[nx][ny]==-1 and L<=abs(G[x][y]-G[nx][ny])<=R:
                ans+=G[nx][ny];q.append((nx,ny));K[nx][ny]=t;z+=1
n,L,R=MIS()
G=[list(MIS()) for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0];A=0
while 1:
    K=[[-1]*n for _ in range(n)]
    P=[[0]*n for _ in range(n)]
    t=0;Z=[]
    for i in range(n):
        for j in range(n):
            if K[i][j]==-1:ans=G[i][j];z=1;K[i][j]=t;bfs();Z.append((ans,z));t+=1
    if t==n**2:print(A);break
    for i in range(n):
        for j in range(n):P[i][j]=int(Z[K[i][j]][0]/Z[K[i][j]][1])
    G=P;A+=1