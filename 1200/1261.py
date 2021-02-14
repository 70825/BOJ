from collections import deque
dx=[0,0,1,-1];dy=[1,-1,0,0]
m,n=map(int,input().split())
miro=[list(map(int,[*input()])) for i in range(n)]
D=[[-1]*m for _ in range(n)];D[0][0]=0
q=deque();q.append((0,0))
while q:
    x,y=q.popleft()
    for i in range(4):
        a,b=x+dx[i],y+dy[i]
        if 0<=a<n and 0<=b<m and D[a][b]==-1:
            if miro[a][b]==0:D[a][b]=D[x][y];q.appendleft((a,b))
            else:D[a][b]=D[x][y]+1;q.append((a,b))
print(D[n-1][m-1])