from collections import deque
from math import log2
input=__import__('sys').stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
lvl = [-1]*n
max_p = int(log2(n))+1
parent = [[-1]*(max_p) for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a-=1; b-=1
    adj[a].append(b)
    adj[b].append(a)

q = deque([0])
lvl[0] = 0
while q:
    x = q.popleft()
    for nx in adj[x]:
        if lvl[nx] == -1:
            parent[nx][0] = x
            lvl[nx] = lvl[x] + 1
            q.append(nx)

for j in range(max_p-1):
    for i in range(1,n):
        if parent[i][j] != -1:
            parent[i][j+1] = parent[parent[i][j]][j]

for i in range(int(input())):
    a, b = map(int,input().split())
    a-=1; b-=1

    if lvl[a] < lvl[b]: a,b = b,a
    diff = lvl[a] - lvl[b]

    j = 0
    while diff:
        if diff % 2: a = parent[a][j]
        diff //= 2
        j += 1
    if a != b:
        for j in range(max_p-1, -1, -1):
            if parent[a][j] != -1 and parent[a][j] != parent[b][j]:
                a = parent[a][j]
                b = parent[b][j]
        a = parent[a][0]
    print(a+1)