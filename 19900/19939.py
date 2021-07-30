n, k = map(int, input().split())
if 2 * n < k * (k + 1):
    print(-1)
    exit()
x = n - k * (k + 1) // 2
print([k, k - 1][x % k == 0])