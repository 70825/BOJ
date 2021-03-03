n=int(input())
D=[*map(int,input().split())]
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if D[i]>D[j]:dp[i]=max(dp[j]+1,dp[i])
print(max(dp))