input=__import__('sys').stdin.readline
n, m = map(int, input().split())
arr = [*map(int, input().split())]

l, r = 0, 10**12
while l <= r:
    mid = (l + r) // 2
    k = sum(mid // arr[i] for i in range(n))
    if k >= m: r = mid - 1
    else: l = mid + 1
print(l)