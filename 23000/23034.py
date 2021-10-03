def find(x):
    if x == p[x]: return p[x]
    p[x] = find(p[x])
    return p[x]

def merge(x, y):
    x, y = find(x), find(y)
    p[y] = x
    return

def dfs(start, now, val):
    for nx, nt in adj[now]:
        if not visit[nx]:
            visit[nx] = 1
            dist[start][nx] = max(val, nt)
            dfs(start, nx, max(val, nt))

input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = []
adj = [[] for _ in range(n + 1)]
p = [i for i in range(n + 1)]
cost = 0
for i in range(m):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
arr.sort(key=lambda a: a[2])
for i in range(m):
    a, b, c = arr[i]
    if find(a) != find(b):
        cost += c
        merge(a, b)
        adj[a].append([b, c])
        adj[b].append([a, c])
dist = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    visit = [0] * (n + 1); visit[i+1] = 1
    dfs(i+1, i+1, 0)
for i in range(int(input())):
    u, v = map(int, input().split())
    print(cost - dist[u][v])