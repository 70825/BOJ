MOD = 998244353
n = int(input())
arr = [*map(int, input().split())]
ans = [0] * n
ans[0] = 1
for i in range(1, n):
    val = 1
    for j in range(i):
        if arr[i] > arr[j]:
            val = (val + ans[j]) % MOD
    ans[i] = val
print(*ans)