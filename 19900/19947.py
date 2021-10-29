def go(cash, year):
    if year == y: return cash

    ret = dp[cash][year]
    if ret != -1: return ret

    if year + 1 <= y: dp[cash][year] = max(dp[cash][year], go(int(cash * 1.05), year+1))
    if year + 3 <= y: dp[cash][year] = max(dp[cash][year], go(int(cash * 1.2), year+3))
    if year + 5 <= y: dp[cash][year] = max(dp[cash][year], go(int(cash * 1.35), year+5))

    return dp[cash][year]

h, y = map(int, input().split())
dp = [[-1] * (y+1) for _ in range(200001)]
print(go(h, 0))