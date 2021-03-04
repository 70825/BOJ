from collections import deque
N,M=map(int,input().split())
Hx,Hy=map(int,input().split())
Ex,Ey=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(N)]
S=[[[-1]*2 for k in range(M)] for _ in range(N)];S[Hx-1][Hy-1][0]=0
q=deque([(Hx-1,Hy-1,0)])
dx,dy=[1,-1,0,0],[0,0,1,-1]
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if D[nx][ny]==0 and S[nx][ny][z]==-1:S[nx][ny][z]=S[x][y][z]+1;q.append((nx,ny,z))
            if z==0 and D[nx][ny]==1 and S[nx][ny][z+1]==-1:S[nx][ny][z+1]=S[x][y][z]+1;q.append((nx,ny,z+1))
a=S[Ex-1][Ey-1][0];b=S[Ex-1][Ey-1][1]
if a==-1 and b==-1:print(-1)
elif a!=-1 and b==-1:print(a)
elif a==-1 and b!=-1:print(b)
else:print(min(a,b))