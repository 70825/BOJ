dp = [[0,0] for _ in range(46)]# A B 개수
dp[0] = [1,0]
for i in range(1,46):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]
k = int(input())
print(*dp[k])