input = __import__('sys').stdin.readline
n, q = map(int, input().split())
arr = sorted([[*map(int, input().split())] + [i] for i in range(n)])
p = [i for i in range(n)]
val = arr[0][1]
idx = arr[0][3]
for i in range(1, n):
    if arr[i][0] <= val:
        val = max(val, arr[i][1])
        p[arr[i][3]] = idx
    else:
        val = arr[i][1]
        idx = arr[i][3]
for i in range(q):
    x, y = map(int, input().split())
    if p[x-1] == p[y-1]: print(1)
    else: print(0)