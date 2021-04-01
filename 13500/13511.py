from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
max_p = 17
adj = [[] for _ in range(n)]
pt = [[-1]*max_p for _ in range(n)]
depth = [-1]*n
cost = [-1]*n

for i in range(n-1):
    a,b,c = map(int,input().split())
    a-=1;b-=1
    adj[a].append([b,c])
    adj[b].append([a,c])

q = deque([0])
cost[0] = 0;depth[0] = 0
while q:
    x = q.popleft()
    for nx,t in adj[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x]+1
            cost[nx] = cost[x] + t
            pt[nx][0] = x
            q.append(nx)

for j in range(max_p-1):
    for i in range(1,n):
        if pt[i][j] != -1:
            pt[i][j+1] = pt[pt[i][j]][j]

for _ in range(int(input())):
    D = [*map(int,input().split())]
    if D[0] == 1:u,v = D[1]-1,D[2]-1
    else: u,v,k = D[1]-1,D[2]-1,D[3]-1
    ou, ov = u,v
    ans = cost[u] + cost[v]
    if depth[u] < depth[v]: u, v = v, u
    diff = depth[u] - depth[v]
    j = 0
    while diff:
        if diff % 2: u = pt[u][j]
        diff //= 2
        j += 1
    if u != v:
        for j in range(max_p-1,-1,-1):
            if pt[u][j] != -1 and pt[u][j] != pt[v][j]:
                u,v = pt[u][j],pt[v][j]
        u = pt[u][j]
    if D[0] == 1: print(ans - 2*cost[u]);continue
    if depth[ou]-depth[u] >= k:
        for j in range(max_p-1,-1,-1):
            if k >= 2**j:
                k -= 2**j;ou = pt[ou][j]
        print(ou+1)
    else:
        k = (depth[ov]-depth[u])-(k - (depth[ou]-depth[u]))
        for j in range(max_p-1,-1,-1):
            if k >= 2**j:
                k -= 2**j;ov = pt[ov][j]
        print(ov+1)