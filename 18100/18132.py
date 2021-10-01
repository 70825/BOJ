MOD = int(1e9) + 7
dp = [0] * 5002
dp[0] = 1
for i in range(1, 5002):
    for j in range(i):
        dp[i] = (dp[i] + (dp[j] * dp[i - j - 1]) % MOD) % MOD
for _ in range(int(input())):
    x = int(input())
    print(dp[x+1])