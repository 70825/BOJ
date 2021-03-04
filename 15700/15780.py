N,K=map(int,input().split())
memo=[*map(int,input().split())]
ans=0
for i in range(K):
    ans+=memo[i]//2
    if memo[i]%2==1:ans+=1
if ans>=N:print('YES')
else:print('NO')