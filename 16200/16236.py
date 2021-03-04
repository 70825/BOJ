from collections import deque
dx,dy = [1,-1,0,0],[0,0,1,-1]
input = __import__('sys').stdin.readline

n = int(input())
D = [[*map(int,input().split())] for _ in range(n)]
ans = 0
lvl = [2,0]
for i in range(n):
    for j in range(n):
        if D[i][j] == 9:
            D[i][j] = 0
            q = deque([[i,j]])
while q:
    x, y = q.popleft()
    S = [[-1]*n for _ in range(n)];S[x][y] = 0
    eq = deque([[x,y]])
    while eq:
        nx,ny = eq.popleft()
        for i in range(4):
            kx,ky = nx+dx[i],ny+dy[i]
            if 0<=kx<n and 0<=ky<n and S[kx][ky] == -1 and D[kx][ky] <= lvl[0]:
                eq.append((kx,ky))
                S[kx][ky] = S[nx][ny] + 1
    food = [-1,-1,float('inf')]
    for i in range(n):
        for j in range(n):
            if S[i][j] != -1 and 1 <= D[i][j] < lvl[0] and food[2] > S[i][j]:
                food = [i,j,S[i][j]]
    if food[0] != -1:
        ans += food[2]
        lvl[1] += 1
        if lvl[0] == lvl[1]:lvl = [lvl[0]+1,0]
        D[food[0]][food[1]] = 0
        q.append((food[0],food[1]))
print(ans)