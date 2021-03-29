from itertools import combinations as cb
from collections import deque

n,m = map(int,input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a-=1;b-=1
    adj[a].append(b)
    adj[b].append(a)
ans = [float('inf')]*3
for (sa,sb) in cb([i for i in range(n)],2):
    S = [float('inf')]*n
    q = deque([sa,sb])
    S[sa] = 0; S[sb] = 0
    while q:
        x = q.popleft()
        for nx in adj[x]:
            if S[x]+2 < S[nx]:q.append(nx);S[nx] = S[x]+2
    k = sum(S)
    sa += 1;sb += 1
    if k < ans[2] or (k == ans[2] and (sa < ans[0] or (sa == ans[0] and sb < ans[1]))):
        ans = [sa,sb,k]
print(*ans)