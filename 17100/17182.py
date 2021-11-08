input = __import__('sys').stdin.readline
from itertools import permutations as pm

n, m = map(int, input().split())
dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    arr = [*map(int, input().split())]
    for j in range(n):
        dist[i][j] = min(dist[i][j], arr[j])
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

res = float('inf')
arr = [i for i in range(n) if i != m]
for path in pm(arr):
    val = 0
    prev = m
    for now in path:
        val += dist[prev][now]
        prev = now
    res = min(res, val)
print(res)