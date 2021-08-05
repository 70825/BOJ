n, k = map(int, input().split())
arr = sorted([int(input()) for i in range(n)], reverse=True)
ans = 0
for i in range(n):
    val = k // arr[i]
    ans += val
    k -= arr[i] * val
print(ans)