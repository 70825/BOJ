from collections import deque
input = __import__('sys').stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
q1, q2 = deque(), deque()
visit1 = [0] * n
visit2 = [0] * n
for i in range(m):
    a, b = map(int, input().split()); a-=1; b-=1
    if i == k - 1:
        q1.append(a); visit1[a] = 1
        q2.append(b); visit2[b] = 1
    else:
        adj[a].append(b)
        adj[b].append(a)
while q1:
    x = q1.popleft()
    for nx in adj[x]:
        if visit1[nx] == 0:
            visit1[nx] = 1
            q1.append(nx)
while q2:
    x = q2.popleft()
    for nx in adj[x]:
        if visit2[nx] == 0:
            visit2[nx] = 1
            q2.append(nx)
if sum(visit1) == n: print(0)
else:print(sum(visit1) * sum(visit2))