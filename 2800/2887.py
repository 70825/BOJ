def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

def merge(x, y):
    x, y = find(x), find(y)
    p[y] = x


__import__('sys').setrecursionlimit(100000)
input = __import__('sys').stdin.readline
n = int(input())
cost = [[*map(int, input().split())] + [_] for _ in range(n)]
path = []
p = [i for i in range(n)]

for i in range(3):
    cost.sort(key=lambda x:x[i])
    for j in range(n-1):
        path.append([cost[j][3], cost[j+1][3], abs(cost[j][i] - cost[j+1][i])])

ans = 0
path.sort(key=lambda x: x[2])
for i in range(len(path)):
    x, y = path[i][0], path[i][1]
    if find(x) != find(y):
        ans += path[i][2]
        merge(x, y)
print(ans)