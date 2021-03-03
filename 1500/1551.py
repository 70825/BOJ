N,K=map(int,input().split())
D=[*map(int,input().split(','))]
for i in range(K):
    memo=[0]*(len(D)-1)
    for j in range(len(D)-1):
        memo[j]=D[j+1]-D[j]
    D=memo
print(','.join(map(str,D)))