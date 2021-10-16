from heapq import *
n = int(input())
arr = [input() for _ in range(n)]
s, e = map(int, input().split())
visit = [float('inf')] * n; visit[s-1] = 0
q = []; heappush(q, [0, s-1])
while q:
    cost, x = heappop(q)
    if cost != visit[x]: continue
    for i in range(n):
        val = cost + sum(abs(int(arr[x][j]) - int(arr[i][j])) ** 2 for j in range(len(arr[x])))
        if i != x and visit[i] > val:
            visit[i] = val
            heappush(q, [val, i])
print(visit[e-1])