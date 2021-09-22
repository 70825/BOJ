input = __import__('sys').stdin.readline
from collections import deque, defaultdict as dfd
item_topology = dfd(lambda : [])
indegree = dfd(lambda: 0)
name = dfd(lambda: 0)

n = int(input())
for i in range(n):
    a, b = input().strip().split()
    indegree[b] += 1
    item_topology[a].append(b)
    name[a], name[b] = 0, 0

q = deque()
next_q = deque()
ans = []
total = len(name.keys())
for x in name.keys():
    if indegree[x] == 0:
        q.append(x)
q = deque(sorted(q))
while q:
    x = q.popleft()
    ans.append(x)
    for nx in item_topology[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            next_q.append(nx)
    if not q:
        q = deque(sorted(next_q))
        next_q = deque()
if len(ans) != total: print(-1)
else: print('\n'.join(ans))