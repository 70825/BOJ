n,m=map(int,input().split())
D=[[0]*(m+1)]+[[0]+[*map(int,input().split())] for _ in range(n)]
K=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        K[i][j]=max(K[i-1][j],K[i][j-1])+D[i][j]
print(K[n][m])