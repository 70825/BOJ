N,K=map(int,input().split())
D=[[0]*(N+1) for _ in range(K+1)]
D[0][0]=1;k=10**9
for i in range(1,K+1):
    for j in range(N+1):
        for l in range(j+1):
            D[i][j]+=D[i-1][j-l]
        D[i][j]%=k
print(D[K][N])