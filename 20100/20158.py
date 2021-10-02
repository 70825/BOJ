from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
input = __import__('sys').stdin.readline

n = int(input())
MAP = [[*map(int, input().split())] for _ in range(n)]
S = [[[[-1] * 15 for ___ in range(4)] for __ in range(n)] for _ in range(n)]
inq = [[[[0] * 15 for ___ in range(4)] for __ in range(n)] for _ in range(n)]
q = deque([[0, 0, 0, 0], [0, 0, 2, 0]]) # x, y, 방향, 가속도
for i in range(4):
    S[0][0][i][0] = 0
while q:
    x, y, d, a = q.popleft()
    inq[x][y][d][a] = 0
    if x == y == n - 1:
        print(S[x][y][d][a])
        exit()
    a += 1
    flag = True
    for i in range(a):
        nx, ny = x + dx[d] * (i + 1), y + dy[d] * (i + 1)
        if nx < 0 or nx >= n or ny < 0 or ny >= n or not (MAP[nx][ny] == 0 or MAP[nx][ny] >= S[x][y][d][a-1]):
            flag = False
            break
    if flag:
        nx, ny = x + dx[d] * a, y + dy[d] * a
        if (MAP[nx][ny] == 0 or S[x][y][d][a-1] + 1 < MAP[nx][ny]) and S[nx][ny][d][a] == -1 and inq[nx][ny][d][a] == 0:
            q.append([nx, ny, d, a])
            S[nx][ny][d][a] = S[x][y][d][a-1] + 1
            inq[nx][ny][d][a] = 1
    for i in range(4):
        if d == i: continue
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and (MAP[nx][ny] == 0 or S[x][y][d][a-1] + 1 < MAP[nx][ny]) and S[nx][ny][i][1] == -1 and inq[nx][ny][d][a] == 0:
            S[nx][ny][i][1] = S[x][y][d][a-1] + 1
            q.append([nx, ny, i, 1])
            inq[nx][ny][i][1] = 1
print('Fired')