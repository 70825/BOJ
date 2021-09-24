input = __import__('sys').stdin.readline
from heapq import *

n = int(input())
station = [*map(int, input().split())]
stations = [[[] for _ in range(station[i])] for i in range(n)]

for i in range(n):
    for j in range(station[i]):
        if j - 1 >= 0: stations[i][j].append((i, j-1))
        if j + 1 < station[i]: stations[i][j].append((i, j+1))

m = int(input())
for i in range(m):
    p1, p2, q1, q2 = map(int, input().split())
    p1-=1; p2-=1; q1-=1; q2-=1
    stations[p1][p2].append((q1, q2))
    stations[q1][q2].append((p1, p2))

for _ in range(int(input())):
    S = [[float('inf')] * station[i] for i in range(n)]
    t, u1, u2, v1, v2 = map(int, input().split())
    u1-=1; u2-=1; v1-=1; v2-=1
    q = []; heappush(q, (u1, u2))
    S[u1][u2] = 0
    while q:
        x, y = heappop(q)
        for nx, ny in stations[x][y]:
            if x == nx and S[nx][ny] > S[x][y] + 1:
                S[nx][ny] = S[x][y] + 1
                heappush(q, (nx, ny))
            elif x != nx and S[nx][ny] > S[x][y] + t:
                S[nx][ny] = S[x][y] + t
                heappush(q, (nx, ny))
    print(S[v1][v2])