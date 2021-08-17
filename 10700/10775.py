def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

input = __import__('sys').stdin.readline
g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
airplane = [int(input()) for _ in range(p)]
ans = 0
for x in airplane:
    val = find(x)
    if val > 0:
        ans += 1
        merge(val, val-1)
    else: break
print(ans)