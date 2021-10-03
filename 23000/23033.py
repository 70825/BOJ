input = __import__('sys').stdin.readline
from heapq import *

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for i in range(m):
    a, b, t, w = map(int, input().split())
    adj[a].append((b, t, w))
q = []; heappush(q, [0, 1])
S = [float('inf')] * (n + 1); S[1] = 0
while q:
    t, x = heappop(q)
    if S[x] != t: continue
    if x == n: print(t); exit()
    for nx, nt, w in adj[x]:
        val = t + nt + (0 if t % w == 0 else w - (t % w))
        if S[nx] > val:
            S[nx] = val
            heappush(q, [val, nx])