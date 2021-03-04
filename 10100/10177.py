for i in range(int(input())):
    N=int(input())
    memo=[[] for j in range(N)]
    for j in range(N):
        memo[j]=[*map(int,input().split())]
    sum_memo=[]
    for j in range(N):
        sum_memo.append(sum(memo[j]))
    for j in range(N):
        ans=0
        for k in range(N):
            ans+=memo[j][k]
        sum_memo.append(ans)
    ans=0;ams=0
    for j in range(N):
        ans+=memo[j][j]
        ams+=memo[N-1-j][j]
    sum_memo.append(ans)
    sum_memo.append(ams)
    if max(sum_memo)==min(sum_memo):print('Magic square of size',N)
    else:print('Not a magic square')