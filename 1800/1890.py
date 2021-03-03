n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
K=[[0]*n for _ in range(n)];K[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:print(K[n-1][n-1]);exit()
        if j+D[i][j]<n:K[i][j+D[i][j]]+=K[i][j]
        if i+D[i][j]<n:K[i+D[i][j]][j]+=K[i][j]