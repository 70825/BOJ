def find(x):
    if x == p[x]: return x
    p[x] = find(p[x])
    return p[x]

def merge(x, y, flag):
    x, y = find(x), find(y)
    arr[x], arr[y] = (arr[x] + arr[y]) if flag else abs(arr[x] - arr[y]), 0
    p[y] = p[x]

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
p = [i for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split()); b-=1; c-=1
    merge(b, c, 1) if a == 1 else merge(b, c, 0)

ans = [arr[i] for i in range(n) if arr[i]]
print(len(ans))
print(*sorted(ans))