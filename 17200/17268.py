input = __import__('sys').stdin.readline
MOD = 987654321

n = int(input())
dp = [0] * 5001
dp[0] = 1
for i in range(1, 5001):
    for j in range(i):
        dp[i] = (dp[i] + (dp[j] * dp[i-j-1]) % MOD) % MOD
print(dp[n//2])