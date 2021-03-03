from collections import deque
n=int(input())
D=[list(map(int,[*input()])) for _ in range(n)]
S=[[-1]*n for _ in range(n)];S[0][0]=0
q=deque([(0,0)])
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and S[nx][ny]==-1:
            if D[nx][ny]==0:q.append((nx,ny));S[nx][ny]=S[x][y]+1
            else:q.appendleft((nx,ny));S[nx][ny]=S[x][y]
print(S[n-1][n-1])