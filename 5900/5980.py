from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
S=[[-1]*m for _ in range(n)]
T=[[] for _ in range(26)];q=deque();ax,ay=0,0
for i in range(n):
    for j in range(m):
        if D[i][j] not in '#.=@':T[ord(D[i][j])-65].append((i,j))
        elif D[i][j]=='=':ax,ay=i,j
        elif D[i][j]=='@':q.append((i,j));S[i][j]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and D[nx][ny]!='#':
            if D[nx][ny] not in '=.@':
                z=ord(D[nx][ny])-65
                if len(T[z])==2:
                    a,b,c,d=T[z][0][0],T[z][0][1],T[z][1][0],T[z][1][1]
                    if T[z][0]==(nx,ny) and S[c][d]==-1:q.append((c,d));S[c][d]=S[x][y]+1
                    elif T[z][1]==(nx,ny) and S[a][b]==-1:q.append((a,b));S[a][b]=S[x][y]+1
            elif D[nx][ny] in '=.' and S[nx][ny]==-1:q.append((nx,ny));S[nx][ny]=S[x][y]+1
print(S[ax][ay])