def dijkstra(s, e):
    q = []; heappush(q, [0, s])
    S = [float('inf')] * (n+1)
    S[s] = 0
    while q:
        t, x = heappop(q)
        if t > S[x]: continue
        for nx, nt in adj[x]:
            if S[nx] > t + nt:
                S[nx] = t + nt
                heappush(q, [t + nt, nx])
    return S[e]

from heapq import *
input = __import__('sys').stdin.readline

n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]
for i in range(e):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])
    adj[v].append([u, w])
arr = [*map(int, input().split())]
s = int(input())

ans = float('inf')
female = 0
prev = arr[0]
for i in range(10):
    fval = dijkstra(prev, arr[i])
    if fval == float('inf'): continue
    female += fval
    prev = arr[i]
    mval = dijkstra(s, arr[i])
    if female >= mval: ans = min(ans, arr[i])
print([-1, ans][ans != float('inf')])