def go(x, y, size, val):
    global ans
    visit[x][y] = 1
    if size % len(s) == 0 and val > ans[0]: ans = [val, x, y]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and MAP[nx][ny] == s[size % len(s)]:
            if visit[nx][ny] and size % len(s) == 0: print(-1); exit()
            go(nx, ny, size + 1, val if size % len(s) else val + 1)
    visit[x][y] = 0

import sys
sys.setrecursionlimit(100000)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m, l = map(int, input().split())
s = input()
MAP = [input() for _ in range(n)]
visit = [[0] * m for _ in range(n)]
ans = [-1, -1, -1]
go(0, 0, 1, 1)
if ans[0] != -1:print(f'{ans[0]}\n{ans[1]+1} {ans[2]+1}')
else: print(-1)