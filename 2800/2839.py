dp = [[float('inf'),float('inf')] for _ in range(5001)] # 3, 5
dp[3] = [1,0];dp[5] = [0,1]
for i in range(6,5001):
    x = dp[i-3]+[]
    y = dp[i-5]+[]
    if sum(x) >= sum(y):
        dp[i] = y
        dp[i][1] += 1
    else:
        dp[i] = x
        dp[i][0] += 1
n = int(input())
if sum(dp[n]) != float('inf'):print(sum(dp[n]))
else:print(-1)