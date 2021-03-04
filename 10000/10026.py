from collections import deque
n=int(input())
D=[list(map(str,[*input()])) for _ in range(n)]
a,b=0,0 #a=일반인,b=적록색약
aS,bS=[[0]*n for _ in range(n)],[[0]*n for _ in range(n)]
q=deque()
dx,dy=[0,0,1,-1],[1,-1,0,0]
for i in range(n):
    for j in range(n):
        if aS[i][j]==0:
            q.append((i,j));aS[i][j]=1;a+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<n and aS[nx][ny]==0 and D[nx][ny]==D[x][y]:
                        q.append((nx,ny));aS[nx][ny]=1
for i in range(n):
    for j in range(n):
        if bS[i][j]==0:
            q.append((i,j));bS[i][j]=1;b+=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<n and bS[nx][ny]==0:
                        if D[x][y] in 'RG' and D[nx][ny] in 'RG':
                            q.append((nx,ny));bS[nx][ny]=1
                        elif D[x][y]==D[nx][ny]=='B':
                            q.append((nx,ny));bS[nx][ny]=1
print(a,b)