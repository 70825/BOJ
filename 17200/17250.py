def find(x):
    if x == p[x]: return x
    p[x] = find(p[x])
    return p[x]

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
p = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split()); a-=1; b-=1
    a, b = find(a), find(b)
    if a == b: print(arr[a])
    else:
        arr[a] += arr[b]; arr[b] = 0; p[b] = a
        print(arr[a])