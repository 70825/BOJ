from collections import deque
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[input() for _ in range(n)]
q=deque([(0,0,0,1,0)])
S=[[[float('inf')]*(k+1) for __ in range(m)] for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0];S[0][0][0]=1
while q:
    x,y,z,t,d=q.popleft()
    if S[x][y][z]!=t:continue
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if D[nx][ny]=='0' and S[nx][ny][z]>t+1:
                S[nx][ny][z]=t+1;q.append((nx,ny,z,t+1,(d+1)%2))
            if z<k and D[nx][ny]=='1':
                if d==0 and S[nx][ny][z+1]>t+1:
                    S[nx][ny][z+1]=t+1;q.append((nx,ny,z+1,t+1,(d+1)%2))
                if d==1 and S[nx][ny][z+1]>t+2:
                    S[nx][ny][z+1]=t+2;q.append((nx,ny,z+1,t+2,d))
k=min(S[n-1][m-1])
print([k,-1][k==float('inf')])