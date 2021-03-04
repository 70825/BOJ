dp = [[0]*30 for _ in range(30)]
for i in range(30):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2,30):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
r,c,w = map(int,input().split())
r-=1;c-=1
ans = 0
for i in range(r,r+w):
    for j in range(1+i-r):
        ans += dp[i][j+c]
print(ans)