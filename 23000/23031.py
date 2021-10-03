input = __import__('sys').stdin.readline
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
n = int(input())
A = input().strip()
MAP = [[*input().strip()] for _ in range(n)]
light = [[0] * n for _ in range(n)]

zombie = []
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 'Z':
            zombie.append([0, i, j])

d, x, y = 0, 0, 0
for i in range(len(A)):
    if A[i] == 'F':
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n: x, y = nx, ny
    elif A[i] == 'L': d = (d + 1) % 4
    else: d = (d + 3) % 4

    if MAP[x][y] == 'S':
        for j in range(x-1, x+2):
            for k in range(y-1, y+2):
                if 0 <= j < n and 0 <= k < n:
                    light[j][k] = 1
    meet = False
    for j in range(len(zombie)):
        di, zx, zy = zombie[j]
        if x == zx and y == zy: meet = True
        nx, ny = zx + dx[di], zy + dy[di]
        if 0 <= nx < n and 0 <= ny < n: zombie[j] = [di, nx, ny]
        else: zombie[j][0] = (di + 2) % 4
        if x == zombie[j][1] and y == zombie[j][2]: meet = True
    if not light[x][y] and meet: print('Aaaaaah!');exit()
print('Phew...')