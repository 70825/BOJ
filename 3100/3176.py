from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
max_p = 17
adj = [[] for _ in range(n)]
depth = [-1]*n
parent = [[-1]*max_p for _ in range(n)]
mxv = [[-1]*max_p for _ in range(n)]
mnv = [[float('inf')]*max_p for _ in range(n)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    a-=1;b-=1
    adj[a].append([b,c])
    adj[b].append([a,c])

q = deque([0])
depth[0] = 0
while q:
    x = q.popleft()
    for nx,t in adj[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            parent[nx][0] = x
            mnv[nx][0] = mxv[nx][0] = t
            q.append(nx)

for j in range(max_p-1):
    for i in range(1,n):
        if parent[i][j] != -1:
            parent[i][j+1] = parent[parent[i][j]][j]
            mnv[i][j+1] = min(mnv[i][j],mnv[parent[i][j]][j])
            mxv[i][j+1] = max(mxv[i][j],mxv[parent[i][j]][j])

for _ in range(int(input())):
    a,b = map(int,input().split())
    a-=1;b-=1
    if depth[a] < depth[b] : a,b = b,a
    diff = depth[a] - depth[b]
    minv, maxv = float('inf'),0
    j = 0
    while diff:
        if diff%2:
            minv = min(minv, mnv[a][j])
            maxv = max(maxv, mxv[a][j])
            a = parent[a][j]
        diff//=2
        j+=1
    if a != b:
        for j in range(max_p-1,-1,-1):
            if parent[a][j] != -1 and parent[a][j] != parent[b][j]:
                minv = min(minv, mnv[a][j], mnv[b][j])
                maxv = max(maxv, mxv[a][j], mxv[b][j])
                a,b = parent[a][j],parent[b][j]
        minv = min(minv, mnv[a][j], mnv[b][j])
        maxv = max(maxv, mxv[a][j], mxv[b][j])
        a = parent[a][j]
    print(minv,maxv)