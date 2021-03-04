D=[[0]*10 for _ in range(1001)]
for i in range(10):D[1][i]=1
N=int(input());k=10007
for i in range(2,N+1):
    for j in range(10):
        D[i][j]+=sum(D[i-1][j:10])%k
print(sum(D[N])%k)