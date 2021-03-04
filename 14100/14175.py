n,m,k=map(int,input().split())
D=[input() for _ in range(n)]
K=['']*(k*n)
for i in range(n):
    for j in range(m):
        for l in range(k):
            K[k*i+l]+=D[i][j]*k
for i in range(k*n):
    print(K[i])