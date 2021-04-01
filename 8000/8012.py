from collections import deque

n = int(input())
max_p = 15
adj = [[] for _ in range(n)]
depth = [-1]*n
parent = [[-1]*max_p for _ in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    a-=1;b-=1
    adj[a].append(b)
    adj[b].append(a)

q=deque([0])
depth[0] = 0
while q:
    x = q.popleft()
    for nx in adj[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            parent[nx][0] = x
            q.append(nx)

for j in range(max_p-1):
    for i in range(1,n):
        if parent[i][j] != -1:
            parent[i][j+1] = parent[parent[i][j]][j]

ans = 0
x = 0
for _ in range(int(input())):
    y = int(input())
    y -= 1
    temp = y
    ans += depth[x] + depth[y]
    if depth[x] < depth[y]: x, y = y, x
    diff = depth[x] - depth[y]
    j = 0
    while diff:
        if diff%2: x = parent[x][j]
        diff //= 2
        j += 1
    if x!=y:
        for j in range(max_p-1,-1,-1):
            if parent[x][j] != - 1 and parent[x][j] != parent[y][j]:
                x, y = parent[x][j], parent[y][j]
        x = parent[x][j]
    ans -= 2*depth[x]
    x = temp
print(ans)