from heapq import *
input = __import__('sys').stdin.readline

v, m = map(int, input().split())
adj = [[] for _ in range(v)]
for i in range(m):
    a, b, c = map(int, input().split())
    a-=1; b-=1
    adj[a].append([b, c])
    adj[b].append([a, c])
J, S = map(int, input().split())
if v == 2 and J != S: print(-1); exit()
J_visit = [float('inf')] * v; J_visit[J-1] = 0
q = []; heappush(q, [0, J-1])
while q:
    t, x = heappop(q)
    if J_visit[x] != t: continue
    for nx, nt in adj[x]:
        if J_visit[nx] > t + nt:
            J_visit[nx] = t + nt
            heappush(q, [t+nt, nx])
S_visit = [float('inf')] * v; S_visit[S-1] = 0
q = []; heappush(q, [0, S-1])
while q:
    t, x = heappop(q)
    if S_visit[x] != t: continue
    for nx, nt in adj[x]:
        if S_visit[nx] > t + nt:
            S_visit[nx] = t + nt
            heappush(q, [t+nt, nx])
min_val = min(J_visit[i]+S_visit[i] for i in range(v) if i != J-1 and i != S-1)
ans = [-1, float('inf')]
for i in range(v):
    if i != J-1 and i != S-1 and J_visit[i] + S_visit[i] == min_val:
        if J_visit[i] <= S_visit[i]:
            if J_visit[i] < ans[1]:
                ans = [i+1, J_visit[i]]
print(ans[0])