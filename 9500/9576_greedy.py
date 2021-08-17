def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

for _ in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n+2)]
    arr = sorted([[*map(int, input().split())] for _ in range(m)], key=lambda x:x[1])
    ans = 0
    for i in range(m):
        a, b = arr[i]
        val = find(a)
        if val <= b:
            merge(val, val+1)
            ans += 1
    print(ans)