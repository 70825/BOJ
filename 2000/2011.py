MOD = 10**6
s = input()
if len(s) == 0: print(0);exit()
dp = [[0]*2 for _ in range(len(s))]
if s[0] == '0': print(0);exit()
if 0 < int(s[0]): dp[0][0] = 1
if len(s) > 1 and 0 < int(s[1]): dp[1][0] = 1
if len(s) > 1 and s[0] != '0' and int(s[0]+s[1]) < 27: dp[1][1] = 1
for i in range(2, len(s)):
    if 0 < int(s[i]): dp[i][0] = sum(dp[i-1]) % MOD
    if s[i-1] != '0' and int(s[i-1]+s[i]) < 27: dp[i][1] = sum(dp[i-2]) % MOD
print(sum(dp[len(s)-1])%MOD)