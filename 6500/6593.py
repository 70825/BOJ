from collections import deque
MAX=27000
dx,dy,dz=[0,0,0,0,1,-1],[0,0,1,-1,0,0],[1,-1,0,0,0,0]
q=deque();E=[]
while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0:break
    D=[[] for _ in range(a)];ans=MAX
    for _ in range(a):
        D[_]=[list(map(str,[*input()])) for __ in range(b)];input()
    S=[[[-1]*c for _ in range(b)] for __ in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if D[i][j][k]=='S':q.append((i,j,k));S[i][j][k]=0
                if D[i][j][k]=='E':E=[i,j,k]
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx<a and 0<=ny<b and 0<=nz<c and D[nx][ny][nz]!='#' and S[nx][ny][nz]==-1:
                q.append((nx,ny,nz))
                S[nx][ny][nz]=S[x][y][z]+1
    x,y,z=E;ans=S[x][y][z]
    print(['Escaped in {} minute(s).'.format(ans),'Trapped!'][ans==MAX or ans==-1])