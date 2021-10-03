input = __import__('sys').stdin.readline
from heapq import *
from collections import defaultdict

n = int(input())
MAP = [defaultdict(lambda: []) for _ in range(n+1)]
arr = [0] + [*map(int, input().split())]
for i in range(1, n+1):
    for j in range(1, arr[i]+1):
        MAP[i][j] = [[i, j-1], [i, j+1]]
for i in range(int(input())):
    p1, p2, q1, q2 = map(int, input().split())
    MAP[p1][p2].append([q1, q2])
    MAP[q1][q2].append([p1, p2])
for i in range(int(input())):
    time, u1, u2, v1, v2 = map(int, input().split())
    q = []; heappush(q, [0, u1, u2])
    S = [defaultdict(lambda: float('inf')) for _ in range(n+1)]
    S[u1][u2] = 0
    while q:
        t, x, y = heappop(q)
        for nx, ny in MAP[x][y]:
            if x == nx and S[nx][ny] > t + 1:
                S[nx][ny] = t + 1
                heappush(q, [t+1, nx, ny])
            if x != nx and S[nx][ny] > t + time:
                S[nx][ny] = t + time
                heappush(q, [t + time, nx, ny])
    print(S[v1][v2])