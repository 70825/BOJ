from heapq import *
n = int(input())
adj = [[] for _ in range(n + 1)]
S = [-1] * (n + 1); S[1] = 0
for i in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
q = [1]
while q:
    x = heappop(q)
    for nx, val in adj[x]:
        if S[nx] == -1 or S[nx] > S[x] + val:
            S[nx] = S[x] + val
            heappush(q, nx)
print(max(S))