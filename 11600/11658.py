def update(i, j, val):
    while i < n + 1:
        p = j
        while p < n + 1:
            tree[i][p] += val
            p += (p & -p)
        i += (i & -i)

def sum_(i, j):
    res = 0
    while i > 0:
        p = j
        while p > 0:
            res += tree[i][p]
            p -= (p & -p)
        i -= (i & -i)
    return res

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
tree = [[0] * (n + 1) for _ in range(n + 1)]
val = [[*map(int, input().split())] for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        update(i, j, val[i-1][j-1])

for i in range(m):
    w, *arr = map(int, input().split())
    if w == 0:
        x, y, c = arr
        update(x, y, c - val[x-1][y-1])
        val[x-1][y-1] = c
    else:
        x1, y1, x2, y2 = arr
        print(sum_(x2, y2) - sum_(x2, y1-1) - sum_(x1-1, y2) + sum_(x1-1, y1-1))