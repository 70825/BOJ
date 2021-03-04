n=int(input())
D=[list(map(int,input().split())) for _ in range(n)]
S=[[0]*n for _ in range(n)];S[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:break
        if i+D[i][j]<n:S[i+D[i][j]][j]+=S[i][j]
        if j+D[i][j]<n:S[i][j+D[i][j]]+=S[i][j]
print(['HaruHaru','Hing'][S[n-1][n-1]==0])