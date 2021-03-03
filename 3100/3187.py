from collections import deque
n,m=map(int,input().split())
D=[input() for _ in range(n)]
S=[[0]*m for _ in range(n)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
a,b=0,0
def bfs(i,j):
    q=deque([(i,j)])
    w,s,S[i][j]=0,0,1
    if D[i][j]=='v':w+=1
    if D[i][j]=='k':s+=1
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny =x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='#' and S[nx][ny]==0:
                if D[nx][ny]=='v':w+=1
                if D[nx][ny]=='k':s+=1
                S[nx][ny]=1;q.append((nx,ny))
    return w,s
for i in range(n):
    for j in range(m):
        if D[i][j]!='#' and S[i][j]==0:
            w,s=bfs(i,j)
            if s>w:a+=s
            else:b+=w
print(a,b)