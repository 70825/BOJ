from heapq import *
input = __import__('sys').stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
MAX = 9876543210

n, t, r, c = map(int, input().split())
MAP = [input() for _ in range(n)]
visit = [[[MAX]*n for _ in range(n)] for __ in range(2)]; visit[0][0][0] = 0
q = []; heappush(q, [0, 0, 0, 0])

while q:
    val, x, y, s = heappop(q)
    if s == 1 and visit[0][x][y] > val: visit[0][x][y] = val
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[0][nx][ny] > val + 1:
            visit[0][nx][ny] = val + 1
            heappush(q, [val+1, nx, ny, 0])
    if s == 0 and visit[1][x][y] > val + t:
        visit[1][x][y] = val + t
        heappush(q, [val+t, x, y, 1])
    if s == 1:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            flag = False
            while 0 <= nx < n and 0 <= ny < n:
                if MAP[nx][ny] == '#': flag = True; break
                nx, ny = nx + dx[i], ny + dy[i]
            if flag and visit[1][nx][ny] > val + 1:
                visit[1][nx][ny] = val + 1
                heappush(q, [val+1, nx, ny, 1])
print(visit[0][r-1][c-1])