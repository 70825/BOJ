from heapq import *
input = __import__('sys').stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
MAX = 987654321

m, n = map(int, input().split())
MAP = [[*map(int, input().split())] for _ in range(m)]
S = [[MAX] * n for _ in range(m)]; S[0][0] = MAP[0][0]
q = []; heappush(q, [MAP[0][0], 0, 0]) # 비용, (x, y)

if MAP[0][0] == -1:
    print(-1)
    exit()

while q:
    t, x, y = heappop(q)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and MAP[nx][ny] != -1 and S[nx][ny] > t + MAP[nx][ny]:
            S[nx][ny] = t + MAP[nx][ny]
            heappush(q, [S[nx][ny], nx, ny])
print([S[m-1][n-1], -1][S[m-1][n-1] == MAX])