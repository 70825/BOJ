from collections import deque
dx,dy=[0,0,1,-1],[-1,1,0,0]
n = int(input())
D = [[*map(int,[*input()])] for _ in range(n)]
C = [[0]*n for _ in range(n)]
K = []; m = 0
for i in range(n):
    for j in range(n):
        z = 0
        if D[i][j]==1 and C[i][j]==0:
            q=deque([[i,j]]);C[i][j]=1
            while q:
                x,y = q.popleft();z+=1
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n and C[nx][ny]==0 and D[nx][ny]==1:
                        q.append([nx,ny]);C[nx][ny]=1
        if z!=0:m+=1;K.append(z)
print(m)
print('\n'.join(map(str,sorted(K))))