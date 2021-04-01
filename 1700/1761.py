from collections import deque
input =__import__('sys').stdin.readline

n = int(input())
max_p = 16 #log2(40000) = 15.xxx
adj = [[] for _ in range(n)]
parent = [[-1]*max_p for _ in range(n)]
for i in range(n-1):
    x,y,d = map(int,input().split())
    x-=1;y-=1
    adj[x].append([y,d])
    adj[y].append([x,d])

q = deque([0])
s = [-1]*n; s[0] = 0
depth = [-1]*n; depth[0] = 0
while q:
    x = q.popleft()
    for nx,d in adj[x]:
        if s[nx] == -1:
            s[nx] = s[x]+d
            depth[nx] = depth[x]+1
            parent[nx][0] = x
            q.append(nx)

for j in range(max_p-1):
    for i in range(1,n):
        if parent[i][j] != -1:
            parent[i][j+1] = parent[parent[i][j]][j]

for _ in range(int(input())):
    x, y = map(int,input().split())
    x-=1; y-=1
    ans = s[x]+s[y]

    if depth[x] < depth[y]: x,y = y,x
    diff = depth[x] - depth[y]

    j = 0
    while diff:
        if diff%2: x = parent[x][j]
        diff //= 2
        j += 1

    if x != y:
        for j in range(max_p-1,-1,-1):
            if parent[x][j] != -1 and parent[x][j] != parent[y][j]:
                x = parent[x][j]
                y = parent[y][j]
        x = parent[x][0]
    print(ans - 2*s[x])