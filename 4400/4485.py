from collections import deque
dx,dy,Max,k=[0,0,-1,1],[1,-1,0,0],10*(10**2),1
while 1:
    n=int(input())
    if n==0:break
    D=[list(map(int,input().split())) for _ in range(n)]
    S=[[Max]*n for _ in range(n)];S[0][0]=D[0][0]
    q=deque([(0,0)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and S[x][y]+D[nx][ny]<S[nx][ny]:
                q.append((nx,ny));S[nx][ny]=S[x][y]+D[nx][ny]
    print('Problem {}: {}'.format(k,S[n-1][n-1]))
    k+=1