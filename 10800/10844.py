D=[[0]*10 for _ in range(101)]
for i in range(1,10):D[1][i]=1
N=int(input());k=10**9
for i in range(2,N+1):
    for j in range(10):
        if j-1>=0:D[i][j]+=D[i-1][j-1]
        if j+1<=9:D[i][j]+=D[i-1][j+1]
        D[i][j]%=k
print(sum(D[N])%k)