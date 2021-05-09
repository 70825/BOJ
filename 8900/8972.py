from collections import deque
dx,dy = [1, 1, 1, 0, 0, 0, -1, -1, -1], [-1, 0, 1]*3
def gg():print(f'kraj {t+1}');exit()

n, m = map(int,input().split())
arr = [[*input()] for _ in range(n)]
move = [*map(int,[*input()])]
enemy = deque()
for x in range(n):
    for y in range(m):
        if arr[x][y] == 'I': sx, sy = x, y
        if arr[x][y] == 'R': enemy.append((x,y))
for t in range(len(move)):
    S = [[0]*m for __ in range(n)]
    sx, sy = sx+dx[move[t]-1], sy+dy[move[t]-1]
    if (sx, sy) in enemy: gg()
    while enemy:
        x, y = enemy.popleft()
        dist = float('inf')
        rx, ry = -1, -1
        for i in range(9):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                z = abs(nx-sx) + abs(ny-sy)
                if dist > z: dist, rx, ry = z, nx, ny
        if dist == 0: gg()
        S[rx][ry]+=1
    new_arr = [['.']*m for _ in range(n)]
    new_arr[sx][sy] = 'I'
    for i in range(n):
        for j in range(m):
            if S[i][j] == 1:enemy.append((i,j));new_arr[i][j] = 'R'
    arr = new_arr
for i in range(n): print(''.join(arr[i]))