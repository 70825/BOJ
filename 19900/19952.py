input = __import__('sys').stdin.readline
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for __ in range(int(input())):
    n, m, o, f, sx, sy, ex, ey = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(o):
        x, y, l = map(int, input().split()); x-=1; y-=1
        arr[x][y] = l
    S = [[-1] * m for _ in range(n)]; S[sx-1][sy-1] = f
    q = deque([[f, sx-1, sy-1]])
    while q:
        p, x, y = q.popleft()
        if S[x][y] != p: continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and S[x][y] - 1 > S[nx][ny] and S[x][y] >= arr[nx][ny] - arr[x][y]:
                S[nx][ny] = S[x][y] - 1
                q.append([S[nx][ny], nx, ny])
    if S[ex-1][ey-1] != -1: print('잘했어!!')
    else: print('인성 문제있어??')